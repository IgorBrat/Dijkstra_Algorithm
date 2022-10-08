from dijkstra.graph import Graph
from dijkstra.vertex import Vertex


class PingResolver:
    def __init__(self, filein: str):
        self.connections = Graph(filein)
        self.pings = []

    def dijkstra(self, start: Vertex):
        pass
