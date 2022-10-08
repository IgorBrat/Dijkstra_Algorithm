from dijkstra.graph import Graph
from dijkstra.vertex import Vertex


class PingResolver:
    def __init__(self, filein: str):
        self.connection = Graph(filein)
        self.pings = []

    def find_min_distance_vertex(self, vertex_path: dict, shortest_distance_set: set):
        min_distance = float('inf')
        for vertex in self.connection.vertexes:
            if vertex_path[vertex] < min_distance and vertex not in shortest_distance_set:
                min_distance = vertex_path[vertex]
                min_distance_vertex = vertex
        return min_distance_vertex

    def dijkstra(self, start: Vertex):
        vertex_path = {start: 0}
        shortest_distance_set = set()
        for vertex in self.connection.vertexes:
            if vertex != start:
                vertex_path[vertex] = float('inf')
        while len(shortest_distance_set) != self.connection.vertexes_count:
            curr_vertex = self.find_min_distance_vertex(vertex_path, shortest_distance_set)
            shortest_distance_set.add(curr_vertex)
            for neighbour in curr_vertex.get_neighbours():
                neighbour_vertex, edge_weight = neighbour
                if vertex_path[curr_vertex] + edge_weight < vertex_path[neighbour_vertex]:
                    vertex_path[neighbour_vertex] = vertex_path[curr_vertex] + edge_weight
        print(vertex_path)
