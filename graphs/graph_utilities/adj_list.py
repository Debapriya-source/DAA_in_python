class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adj_list[source].append(destination)
            # Uncomment for undirected graph
            # self.adj_list[destination].append(source)

    def remove_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            if destination in self.adj_list[source]:
                self.adj_list[source].remove(destination)
            # Uncomment for undirected graph
            # if source in self.adj_list[destination]:
            #     self.adj_list[destination].remove(source)

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
    graph = Graph(num_vertices)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    print("Unweighted graph adjacency list:")
    graph.print_graph()

    vertex = 2
    neighbors = graph.get_neighbors(vertex)
    print(f"Neighbors of vertex {vertex}: {neighbors}")
