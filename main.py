from dijkstra.graph import Graph
from dijkstra.ping_resolver import PingResolver


def main():
    relative_path = "resources/"
    pr = PingResolver(f"{relative_path}input.txt")


if __name__ == '__main__':
    main()
