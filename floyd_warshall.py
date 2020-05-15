from math import inf


def get_apsp(graph):
    result = [None]

    for node in range(1, len(graph)):
        result.append([inf for _ in range(len(graph))])

    for node in range(1, len(graph)):
        for neighbour, weight in graph[node]:
            result[neighbour][node] = weight
        result[node][node] = 0

    for k in range(1, len(graph)):
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                result[j][i] = min(result[j][i], result[j][k] + result[k][i])

    return result
