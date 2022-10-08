from dijkstra.graph import Graph
from dijkstra.ping_resolver import PingResolver


def main():
    relative_path = "resources/"
    pr = PingResolver(f"{relative_path}input.txt")
    pr.dijkstra(pr.connection.vertexes[0])


if __name__ == '__main__':
    main()
