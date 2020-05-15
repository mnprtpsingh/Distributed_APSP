from random import randint, shuffle


def create_graph(max_nodes):
    number_of_nodes, graph = randint(2, max_nodes), [None]

    for node in range(1, number_of_nodes + 1):
        graph.append([])

        nodes = list(range(1, number_of_nodes + 1))
        shuffle(nodes)

        out_degree = randint(2, max(2, number_of_nodes >> 2))
        neighbours = sorted(nodes[:out_degree + 1])

        for neighbour in neighbours:
            if neighbour != node:
                weight = randint(0, number_of_nodes >> 1)
                graph[node].append((neighbour, weight))

    return graph
