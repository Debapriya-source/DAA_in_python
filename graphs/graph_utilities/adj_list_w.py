class WeightedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adj_list[source].append((destination, weight))
            # Uncomment for undirected graph
            # self.adj_list[destination].append((source, weight))

    def remove_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adj_list[source] = [
                (dest, weight) for dest, weight in self.adj_list[source] if dest != destination]
            # Uncomment for undirected graph
            # self.adj_list[destination] = [(src, weight) for src, weight in self.adj_list[destination] if src != source]

    def print_graph(self):
        for vertex, neighbors in enumerate(self.adj_list):
            print(f"Vertex {vertex}: {neighbors}")

    def get_neighbors(self, vertex):
        if 0 <= vertex < self.vertices:
            return self.adj_list[vertex]
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

    print("Weighted graph adjacency list:")
    graph.print_graph()

    vertex = 2
    neighbors = graph.get_neighbors(vertex)
    print(f"Neighbors of vertex {vertex}: {neighbors}")
