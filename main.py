from dijkstra.ping_resolver import PingResolver


def main():
    relative_path = "resources/"

    pr = PingResolver(f"{relative_path}gamesrv.in", f"{relative_path}gamesrv.out")
    pr.get_minimum_ping()

    pr1 = PingResolver(f"{relative_path}gamesrv1.in", f"{relative_path}gamesrv1.out")
    pr1.get_minimum_ping()

    pr2 = PingResolver(f"{relative_path}gamesrv2.in", f"{relative_path}gamesrv2.out")
    pr2.get_minimum_ping()


if __name__ == '__main__':
    main()
