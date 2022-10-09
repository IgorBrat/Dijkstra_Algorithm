from dijkstra.graph import Graph
from dijkstra.vertex import Vertex


class PingResolver:
    def __init__(self, filein: str, fileout: str):
        print(f"Started working with {filein}...")
        self.connection = Graph(filein)
        self.fileout = fileout

    def __find_min_distance_vertex(self, vertex_path: dict, shortest_distance_set: set):
        min_distance = float('inf')
        for vertex in self.connection.vertexes:
            if vertex_path[vertex] < min_distance and vertex not in shortest_distance_set:
                min_distance = vertex_path[vertex]
                min_distance_vertex = vertex
        return min_distance_vertex

    def __dijkstra(self, start: Vertex):
        vertex_path = {start: 0}
        shortest_distance_set = set()
        for vertex in self.connection.vertexes:
            if vertex != start:
                vertex_path[vertex] = float('inf')
        while len(shortest_distance_set) != self.connection.vertexes_count:
            curr_vertex = self.__find_min_distance_vertex(vertex_path, shortest_distance_set)
            shortest_distance_set.add(curr_vertex)
            for neighbour in curr_vertex.get_neighbours():
                neighbour_vertex, edge_weight = neighbour
                if vertex_path[curr_vertex] + edge_weight < vertex_path[neighbour_vertex]:
                    vertex_path[neighbour_vertex] = vertex_path[curr_vertex] + edge_weight
        return vertex_path

    def get_minimum_ping(self):
        """
        Place server on some router so that among minimum pings to clients the biggest one
        will be the smallest while replacing server to other router
        :return: the smallest max ping
        """
        max_ping_list = []
        for vertex in self.connection.vertexes:
            if vertex.value not in self.connection.clients:
                curr_vertex_path = self.__dijkstra(vertex)
                curr_pings_list = []
                for curr_vertex, distance in curr_vertex_path.items():
                    if curr_vertex.value in self.connection.clients:
                        curr_pings_list.append(distance)
                max_ping_list.append(max(curr_pings_list))
        self.__write_res_to_file(min(max_ping_list))
        return min(max_ping_list)

    def __write_res_to_file(self, res: int):
        with open(self.fileout, "w") as fileout:
            fileout.write("Minimum max ping: " + str(res))
        print(f"Successfully written result to file {self.fileout}")

    def print_connection(self):
        self.connection.print()
