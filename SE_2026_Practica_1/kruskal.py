class KruskalCityNetwork:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Función para encontrar el conjunto de un elemento (con compresión de ruta)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Función para unir dos conjuntos (por rango)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def apply_kruskal(self):
        result = []  # Aquí guardaremos el MST
        i, e = 0, 0
        
        # 1. Ordenar todas las aristas por peso (costo) de menor a mayor
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            # 2. Tomar la arista más barata
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # 3. Si no forma un ciclo, incluirla
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Mostrar resultados
        print("Conexiones sugeridas para minimizar costos:")
        costo_total = 0
        for u, v, weight in result:
            costo_total += weight
            print(f"Ciudad {u} -- Ciudad {v} == Costo: ${weight}M")
        print(f"\nCosto Total de la Red: ${costo_total}M")

# --- CASO DE USO REAL ---
# Supongamos 5 ciudades (0 a 4)
# Las aristas representan la distancia/costo entre ellas
red = KruskalCityNetwork(5)
red.add_edge(0, 1, 10) # Ciudad 0 a 1 cuesta 10
red.add_edge(0, 2, 6)
red.add_edge(0, 3, 5)
red.add_edge(1, 3, 15)
red.add_edge(2, 3, 4)
red.add_edge(3, 4, 8)

red.apply_kruskal()