import heapq

def dijkstra(grafo, inicio):
    # Diccionario para guardar la distancia mínima a cada lugar
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    
    # Cola de prioridad: (distancia_acumulada, nodo_actual)
    prioridad = [(0, inicio)]
    
    while prioridad:
        distancia_actual, nodo_actual = heapq.heappop(prioridad)

        # Si ya encontramos un camino mejor antes, ignoramos este
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Revisamos los vecinos del lugar actual
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            # Si este nuevo camino es más corto, lo guardamos
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(prioridad, (distancia, vecino))
    
    return distancias

# --- Aplicación a la vida cotidiana ---
# Los números representan minutos de trayecto
mapa_ciudad = {
    'Casa': {'Café': 5, 'Gasolinera': 10},
    'Café': {'Gimnasio': 10, 'Oficina': 20},
    'Gasolinera': {'Gimnasio': 2},
    'Gimnasio': {'Oficina': 5},
    'Oficina': {}
}

resultado = dijkstra(mapa_ciudad, 'Casa')

print("Minutos mínimos desde Casa:")
for lugar, tiempo in resultado.items():
    print(f"-> A {lugar}: {tiempo} min")