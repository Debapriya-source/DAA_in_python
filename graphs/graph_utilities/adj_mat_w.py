class WeightedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        # self.adj_matrix = [[float("inf")] * vertices for _ in range(vertices)]
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adj_matrix[source][destination] = weight
            # Uncomment for undirected graph
            # self.adj_matrix[destination][source] = weight

    def remove_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            # self.adj_matrix[source][destination] = float("inf")
            self.adj_matrix[source][destination] = 0
            # Uncomment for undirected graph
            # self.adj_matrix[destination][source] = float("inf")
            # self.adj_matrix[destination][source] = 0

    def print_graph(self):
        for row in self.adj_matrix:
            # print(" ".join(map(lambda x: "∞" if x == float("inf") else str(x), row)))
            print(row)

    def get_neighbors(self, vertex):
        if 0 <= vertex < self.vertices:
            # neighbors = [(index, weight) for index, weight in enumerate(
            #     self.adj_matrix[vertex]) if weight != float("inf")]
            neighbors = [(index, weight) for index, weight in enumerate(
                self.adj_matrix[vertex]) if weight != 0]
            return neighbors
        else:
            return []


if __name__ == "__main__":
    num_vertices = 5
    graph = WeightedGraph(num_vertices)

    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 3, 2)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 4, 1)

    print("Weighted graph adjacency matrix:")
    graph.print_graph()

    vertex = 2
    neighbors = graph.get_neighbors(vertex)
    print(f"Neighbors of vertex {vertex}: {neighbors}")
