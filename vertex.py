from __future__ import annotations


class Vertex:
    def __init__(self, value: int):
        self.value = value
        self._neighbours = set()

    def add_neighbour(self, neighbour: Vertex, edge_weight: int):
        self._neighbours.add((neighbour, edge_weight))

    def get_neighbours(self):
        return self._neighbours

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(int(self.value))

    def __repr__(self):
        return f"V:{self.value}"
