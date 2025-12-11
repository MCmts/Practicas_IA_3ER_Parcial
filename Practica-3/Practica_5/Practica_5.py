class UnionFind:
    def __init__(self, n):
        self.padre = {i: i for i in n}

    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.padre[rb] = ra
            return True
        return False


def kruskal(grafo, minimo=True):
    print("\n--- Simulador del algoritmo de Kruskal ---")
    print("Modo:", "Árbol de Mínimo Costo" if minimo else "Árbol de Máximo Costo")

    # ordenar aristas
    edges = []
    for u in grafo:
        for v, w in grafo[u]:
            if (v, u, w) not in edges:  # evitar duplicados
                edges.append((u, v, w))

    edges.sort(key=lambda x: x[2], reverse=not minimo)

    print("\nAristas ordenadas:")
    for u, v, w in edges:
        print(f"({u} -- {v}) peso {w}")

    uf = UnionFind(grafo.keys())
    apm = []
    total = 0

    print("\n--- PASO A PASO ---")
    for u, v, w in edges:
        print(f"\n¿Agregamos ({u} -- {v}) peso {w}?")
        if uf.union(u, v):
            print("✔ Sí, no forma ciclo. Se agrega.")
            apm.append((u, v, w))
            total += w
        else:
            print("✘ No, forma ciclo. Se descarta.")

    print("\n--- RESULTADO FINAL ---")
    for u, v, w in apm:
        print(f"{u} -- {v} : {w}")

    print(f"\nCosto total: {total}\n")
    return apm


# Ejemplo de grafo
grafo = {
    "A": [("B", 4), ("C", 3)],
    "B": [("A", 4), ("C", 1), ("D", 2)],
    "C": [("A", 3), ("B", 1), ("D", 4)],
    "D": [("B", 2), ("C", 4)]
}

kruskal(grafo, minimo=True)
kruskal(grafo, minimo=False)