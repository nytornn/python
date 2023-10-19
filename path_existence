class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # Pro neorientovaný graf

    def is_reachable(self, u, v):
        return self.adj_matrix[u][v] == 1

# Příklad použití
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)

u = 2
v = 0

if g.is_reachable(u, v):
    print(f"Cesta mezi uzly {u} a {v} existuje.")
else:
    print(f"Cesta mezi uzly {u} a {v} neexistuje.")
