import sys

def dijkstra(graph, start):
    # Inicialización
    nodes = list(graph.keys())
    unvisited = nodes.copy()
    distances = {node: float('inf') for node in nodes}
    previous = {node: None for node in nodes}
    distances[start] = 0

    print(f"Distancias iniciales: {distances}\n")

    while unvisited:
        # Nodo con menor distancia
        current = min((node for node in unvisited), key=lambda node: distances[node])
        unvisited.remove(current)

        print(f"Nodo actual: {current}, Distancia acumulada: {distances[current]}")

        for neighbor, weight in graph[current].items():
            alt = distances[current] + weight
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous[neighbor] = current
                print(f"  Actualizando distancia de {neighbor} a {alt} (vía {current})")
        print(f"Distancias hasta ahora: {distances}\n")

    return distances, previous

# Grafo de ejemplo (diccionario)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

distances, previous = dijkstra(graph, 'A')
print("Distancias finales:", distances)
print("Predecesores:", previous)