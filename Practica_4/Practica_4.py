import heapq

def prim(grafo, inicio):
    visitado = set()
    apm = []
    total = 0
    cola = [(0, inicio, None)]

    print("\n--- Simulación del Algoritmo de Prim ---\n")

    while cola:
        costo, nodo, padre = heapq.heappop(cola)

        if nodo in visitado:
            continue

        visitado.add(nodo)

        if padre is not None:
            print(f"Se agrega la arista ({padre} -- {nodo}) con costo {costo}")
            apm.append((padre, nodo, costo))
            total += costo

        for vecino, peso in grafo[nodo]:
            if vecino not in visitado:
                heapq.heappush(cola, (peso, vecino, nodo))

    print("\nÁrbol Parcial Mínimo obtenido:")
    for u, v, w in apm:
        print(f"{u} -- {v} : {w}")

    print(f"\nCosto total del APM: {total}")
    return apm

# Ejemplo de grafo
grafo = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)]
}

prim(grafo, "A")