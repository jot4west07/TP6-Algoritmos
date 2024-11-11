from cola import Queue
from heap import HeapMin
from pila import Stack
from grafo import Graph

# Crear grafo no dirigido
grafo_casa = Graph(dirigido=False)

# Lista de ambientes
ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
    "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
]

# Agregar vértices al grafo
for ambiente in ambientes:
    grafo_casa.insert_vertice(ambiente)

# Lista de conexiones entre ambientes con distancias en metros
aristas = [
    ("cocina", "comedor", 3),
    ("cocina", "baño 1", 5),
    ("cocina", "habitación 1", 10),
    ("comedor", "sala de estar", 6),
    ("comedor", "terraza", 7),
    ("comedor", "patio", 8),
    ("cochera", "habitación 1", 12),
    ("cochera", "patio", 15),
    ("quincho", "terraza", 4),
    ("quincho", "patio", 5),
    ("baño 1", "baño 2", 2),
    ("habitación 1", "habitación 2", 6),
    ("habitación 2", "sala de estar", 5),
    ("sala de estar", "terraza", 9),
    ("terraza", "patio", 3),
    ("patio", "cocina", 10),
]

# Agregar las aristas al grafo
for origen, destino, distancia in aristas:
    grafo_casa.insert_arista(origen, destino, distancia)

# Obtener el árbol de expansión mínima
arbol_expansion_minima = grafo_casa.kruskal("cocina")  # El punto de origen es opcional en Kruskal ya que el grafo es no dirigido

# Calcular la longitud total de cable en metros
longitud_total_cable = 0
for conexion in arbol_expansion_minima:
    partes = conexion.split(";")
    for arista in partes:
        partes_arista = arista.split("-")
        if len(partes_arista) == 3:
            longitud_total_cable += int(partes_arista[2])

print(f"Total de metros de cable necesarios para conectar todos los ambientes: {longitud_total_cable} metros")

# Encontrar el camino más corto desde "habitación 1" hasta "sala de estar"
# La pila camino_a_sala_estar almacena los vértices y la distancia acumulada hasta llegar a cada uno de ellos desde "habitación 1"
camino_a_sala_estar = grafo_casa.dijkstra("habitación 1")

# Calcular la distancia total del camino hasta "sala de estar"
# Inicializa la variable distancia_a_sala_estar en 0. Esta variable se utilizará para almacenar la distancia acumulada más corta encontrada entre "habitación 1" y "sala de estar".
distancia_a_sala_estar = 0
while camino_a_sala_estar.size() > 0:
    # La función pop() extrae el elemento superior de la pila (el nodo más reciente en el camino) y lo guarda en paso. 
    paso = camino_a_sala_estar.pop()
    # 1_ paso[0]: La distancia acumulada desde "habitación 1" hasta el nodo actual.
    # 2_ paso[1]: La información del nodo actual (valor del ambiente, nodo en sí, y vértice anterior).
    
    if paso[1][0] == "sala de estar":
        distancia_a_sala_estar = paso[0]
        break

print(f"Distancia del camino más corto desde 'habitación 1' hasta 'sala de estar': {distancia_a_sala_estar} metros")

