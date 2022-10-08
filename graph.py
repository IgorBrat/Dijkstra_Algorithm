from dijkstra.vertex import Vertex


class Graph:
    def __init__(self, filein: str):
        self.vertexes = []
        self.__read_input(filein)

    def __read_input(self, filein: str):
        with open(filein) as file:
            lines = file.read().splitlines()
        self.vertexes_count = int(lines[0].split(" ")[0])
        self.edges_count = int(lines[0].split(" ")[1])
        self.clients = [int(client) for client in lines[1].split(" ")]
        for i in range(self.edges_count):
            start_vertex, end_vertex, edge_weight = lines[i + 2].split(" ")
            start = Vertex(int(start_vertex))
            end = Vertex(int(end_vertex))
            if start not in self.vertexes:
                start.add_neighbour(end, int(edge_weight))
                self.vertexes.append(start)
            else:
                vertex = self.find_vertex(start)
                vertex.add_neighbour(end, int(edge_weight))
            if end not in self.vertexes:
                end.add_neighbour(start, int(edge_weight))
                self.vertexes.append(end)
            else:
                vertex = self.find_vertex(end)
                vertex.add_neighbour(start, int(edge_weight))

    def find_vertex(self, other: Vertex):
        for vertex in self.vertexes:
            if vertex == other:
                return vertex

    def print(self):
        for vertex in self.vertexes:
            print(vertex)
