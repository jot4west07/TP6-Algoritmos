from cola import Queue
from heap import HeapMin
from pila import Stack
from grafo import Graph  

# Crear el grafo
# Las maravillas arquitectonicas estan relacionadas a un solo pais
maravillas_architectonicas = [
    {"nombre": "Gran Muralla China", "pais": "China", "tipo": "arquitectónica"},
    {"nombre": "Petra", "pais": "Jordania", "tipo": "arquitectónica"},
    {"nombre": "Cristo Redentor", "pais": "Brasil", "tipo": "arquitectónica"},
    {"nombre": "Machu Picchu", "pais": "Perú", "tipo": "arquitectónica"},
    {"nombre": "Chichén Itzá", "pais": "México", "tipo": "arquitectónica"},
    {"nombre": "Coliseo Romano", "pais": "Italia", "tipo": "arquitectónica"},
    {"nombre": "Taj Mahal", "pais": "India", "tipo": "arquitectónica"}
]

# Algunas maravillas naturales tienen varios paises
maravillas_naturales = [
    {"nombre": "Amazonas", "pais": ["Brasil", "Perú", "Colombia"], "tipo": "natural"},
    {"nombre": "Halong Bay", "pais": "Vietnam", "tipo": "natural"},
    {"nombre": "Iguazú", "pais": ["Brasil", "Argentina"], "tipo": "natural"},
    {"nombre": "Islas Galápagos", "pais": "Ecuador", "tipo": "natural"},
    {"nombre": "Jeju Island", "pais": "Corea del Sur", "tipo": "natural"},
    {"nombre": "Komodo", "pais": "Indonesia", "tipo": "natural"},
    {"nombre": "Puerto Princesa Underground River", "pais": "Filipinas", "tipo": "natural"}
]

# Crear un grafo no dirigido
grafo_architectonico = Graph(dirigido=False)
grafo_natural = Graph(dirigido=False)

# Añadir las maravillas arquitectónicas al grafo
for maravilla in maravillas_architectonicas:
    grafo_architectonico.insert_vertice(maravilla['nombre'])

# Añadir las maravillas naturales al grafo
for maravilla in maravillas_naturales:
    grafo_natural.insert_vertice(maravilla['nombre'])

# Distancias inventadas (en km) entre cada par de maravillas del mismo tipo
distancias_architectonicas = {
    ("Gran Muralla China", "Petra"): 6000,
    ("Gran Muralla China", "Cristo Redentor"): 19000,
    ("Gran Muralla China", "Machu Picchu"): 12000,
    ("Gran Muralla China", "Chichén Itzá"): 13000,
    ("Gran Muralla China", "Coliseo Romano"): 8000,
    ("Gran Muralla China", "Taj Mahal"): 5000,
    ("Petra", "Cristo Redentor"): 9000,
    ("Petra", "Machu Picchu"): 10000,
    ("Petra", "Chichén Itzá"): 7000,
    ("Petra", "Coliseo Romano"): 5000,
    ("Petra", "Taj Mahal"): 4000,
    ("Cristo Redentor", "Machu Picchu"): 15000,
    ("Cristo Redentor", "Chichén Itzá"): 16000,
    ("Cristo Redentor", "Coliseo Romano"): 12000,
    ("Cristo Redentor", "Taj Mahal"): 20000,
    ("Machu Picchu", "Chichén Itzá"): 3000,
    ("Machu Picchu", "Coliseo Romano"): 7000,
    ("Machu Picchu", "Taj Mahal"): 8000,
    ("Chichén Itzá", "Coliseo Romano"): 4000,
    ("Chichén Itzá", "Taj Mahal"): 6000,
    ("Coliseo Romano", "Taj Mahal"): 9000
}

distancias_naturales = {
    ("Amazonas", "Halong Bay"): 20000,
    ("Amazonas", "Iguazú"): 10000,
    ("Amazonas", "Islas Galápagos"): 15000,
    ("Amazonas", "Jeju Island"): 25000,
    ("Amazonas", "Komodo"): 18000,
    ("Amazonas", "Puerto Princesa Underground River"): 22000,
    ("Halong Bay", "Iguazú"): 15000,
    ("Halong Bay", "Islas Galápagos"): 17000,
    ("Halong Bay", "Jeju Island"): 12000,
    ("Halong Bay", "Komodo"): 13000,
    ("Halong Bay", "Puerto Princesa Underground River"): 14000,
    ("Iguazú", "Islas Galápagos"): 8000,
    ("Iguazú", "Jeju Island"): 10000,
    ("Iguazú", "Komodo"): 12000,
    ("Iguazú", "Puerto Princesa Underground River"): 14000,
    ("Islas Galápagos", "Jeju Island"): 14000,
    ("Islas Galápagos", "Komodo"): 18000,
    ("Islas Galápagos", "Puerto Princesa Underground River"): 19000,
    ("Jeju Island", "Komodo"): 16000,
    ("Jeju Island", "Puerto Princesa Underground River"): 20000,
    ("Komodo", "Puerto Princesa Underground River"): 22000
}

# Añadir las aristas con las distancias correspondientes para maravillas arquitectónicas
for (origen, destino), distancia in distancias_architectonicas.items():
    grafo_architectonico.insert_arista(origen, destino, distancia)
    grafo_architectonico.insert_arista(destino, origen, distancia)  # Aseguramos que sea bidireccional

# Añadir las aristas con las distancias correspondientes para maravillas naturales
for (origen, destino), distancia in distancias_naturales.items():
    grafo_natural.insert_arista(origen, destino, distancia)
    grafo_natural.insert_arista(destino, origen, distancia)  # Aseguramos que sea bidireccional

# 3. Hallar el árbol de expansión mínimo de cada tipo de maravillas
def obtener_arbol_expansion_minima(grafo):
    return grafo.kruskal(None)

# Obtener los árboles de expansión mínima de cada tipo
arbol_expansion_architectonico = obtener_arbol_expansion_minima(grafo_architectonico)
arbol_expansion_natural = obtener_arbol_expansion_minima(grafo_natural)

# 4. Determinar si existen países que dispongan de maravillas arquitectónicas y naturales
def paises_con_marquillas_arquitectonicas_y_naturales():
    # Set almacena una colección de elementos únicos y desordenados, no se permiten duplicados
    paises_arquitectonicos = set()
    paises_naturales = set()

    # Añadir países con maravillas arquitectónicas
    for maravilla in maravillas_architectonicas:
        paises_arquitectonicos.add(maravilla['pais'])

    # Añadir países con maravillas naturales
    for maravilla in maravillas_naturales:
        if isinstance(maravilla['pais'], list):  # Si hay varios países
            for pais in maravilla['pais']:
                paises_naturales.add(pais)
        else:  # Si solo hay un país
            paises_naturales.add(maravilla['pais'])

    paises_comunes = paises_arquitectonicos.intersection(paises_naturales)
    return paises_comunes

# 5. Determinar si algún país tiene más de una maravilla del mismo tipo
def paises_con_multiples_maravillas_por_tipo():
    paises_arquitectonicos = {}
    paises_naturales = {}

    # Contamos las maravillas arquitectónicas por país
    for maravilla in maravillas_architectonicas:
        pais = maravilla['pais']
        if pais in paises_arquitectonicos:
            paises_arquitectonicos[pais] += 1
        else:
            paises_arquitectonicos[pais] = 1

    # Contamos las maravillas naturales por país
    for maravilla in maravillas_naturales:
        if isinstance(maravilla['pais'], list):  # Si hay varios países
            for pais in maravilla['pais']:
                if pais in paises_naturales:
                    paises_naturales[pais] += 1
                else:
                    paises_naturales[pais] = 1
        else:  # Si solo hay un país
            pais = maravilla['pais']
            if pais in paises_naturales:
                paises_naturales[pais] += 1
            else:
                paises_naturales[pais] = 1

    # Filtramos países con más de una maravilla
    # Count asume el nro de maravillas del pais
    multiples_arquitectonicas = {pais for pais, count in paises_arquitectonicos.items() if count > 1}
    multiples_naturales = {pais for pais, count in paises_naturales.items() if count > 1}

    return multiples_arquitectonicas, multiples_naturales


# Obtener los países con múltiples maravillas
multiples_arquitectonicas, multiples_naturales = paises_con_multiples_maravillas_por_tipo()

# Mostrar resultados
print("Árbol de Expansión Mínimo de las Maravillas Arquitectónicas:")
print(arbol_expansion_architectonico)
print("")

print("Árbol de Expansión Mínimo de las Maravillas Naturales:")
print(arbol_expansion_natural)
print("")

print("Países con maravillas arquitectónicas y naturales:")
print(paises_con_marquillas_arquitectonicas_y_naturales())
print("")

# Mostrar el resultado de países con múltiples maravillas
if multiples_arquitectonicas:
    print("Países con múltiples maravillas arquitectónicas:")
    print(multiples_arquitectonicas)
    print("")
else:
    print("No hay países con múltiples maravillas arquitectónicas.")
    print("")

if multiples_naturales:
    print("Países con múltiples maravillas naturales:")
    print(multiples_naturales)
    print("")
else:
    print("No hay países con múltiples maravillas naturales.")
    print("")
