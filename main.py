from dijkstra.ping_resolver import PingResolver


def main():
    relative_path = "resources/"

    pr = PingResolver(f"{relative_path}input.txt", f"{relative_path}output.txt")
    pr.get_minimum_ping()

    pr1 = PingResolver(f"{relative_path}input1.txt", f"{relative_path}output1.txt")
    pr1.get_minimum_ping()

    pr2 = PingResolver(f"{relative_path}input2.txt", f"{relative_path}output2.txt")
    pr2.get_minimum_ping()


if __name__ == '__main__':
    main()
