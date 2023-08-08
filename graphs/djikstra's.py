class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2

        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest][0]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest][0]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


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


def dijkstra(graph, start_vertex):
    distances = [float('inf')] * graph.vertices
    distances[start_vertex] = 0
    # To store the previous vertex for each vertex
    previous = [-1] * graph.vertices

    visited = set()
    heap = MinHeap()
    heap.push((0, start_vertex))

    while heap.heap:
        current_distance, current_vertex = heap.pop()

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heap.push((distance, neighbor))

    return distances, previous


def shortest_path(previous, start_vertex, end_vertex):
    path = []
    current_vertex = end_vertex
    # print(current_vertex)
    while current_vertex is not None:
        # print(current_vertex, previous[current_vertex])
        path.insert(0, current_vertex)
        current_vertex = previous[current_vertex]
        if current_vertex == start_vertex:
            path.insert(0, start_vertex)
            return path
    return path


if __name__ == "__main__":
    num_vertices = 6
    graph = WeightedGraph(num_vertices)

    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 8)
    graph.add_edge(2, 4, 10)
    graph.add_edge(3, 4, 2)
    graph.add_edge(3, 5, 6)
    graph.add_edge(4, 5, 3)

    # start_vertex = 0
    # shortest_distances = dijkstra(graph, start_vertex)

    # target_vertex = 5
    # shortest_distances, previous_vertices = dijkstra(graph, start_vertex)
    # shortest_path = print_shortest_path(previous_vertices, target_vertex)

    # print(
    #     f"Shortest path from vertex {start_vertex} to vertex {target_vertex}: {shortest_path}")
    # print(
    #     f"Shortest distance to vertex {target_vertex}: {shortest_distances[target_vertex]}")

    start_vertex = 0
    end_vertex = 4
    shortest_distances, previous = dijkstra(graph, start_vertex)

    path = shortest_path(previous, start_vertex, end_vertex)
    print(
        f"Shortest path from vertex {start_vertex} to vertex {end_vertex}: {path}")
    # print(previous)
