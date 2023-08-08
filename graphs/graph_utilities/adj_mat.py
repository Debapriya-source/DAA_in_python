class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        # initialize the matrix with zeros vXv
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adj_matrix[source][destination] = 1
            # comment for undirected graph
            self.adj_matrix[destination][source] = 1

    def remove_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adj_matrix[source][destination] = 0
            # comment for undirected graph
            self.adj_matrix[destination][source] = 0

    def print_graph(self):
        for row in self.adj_matrix:
            # print(" ".join(map(str, row)))
            print(row, "\n")

    def get_neighbors(self, vertex):
        if 0 <= vertex < self.vertices:
            neighbors = [index for index, value in enumerate(
                self.adj_matrix[vertex]) if value == 1]
            return neighbors
        else:
            return []


if __name__ == "__main__":
    num_vertices = 6
    graph = Graph(num_vertices)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 5)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)

    print("Graph adjacency matrix:")
    graph.print_graph()

    vertex = 2
    neighbors = graph.get_neighbors(vertex)
    print(f"Neighbors of vertex {vertex}: {neighbors}")
