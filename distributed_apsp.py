from math import inf


def initilisation(graph, distance, estimate, message):

    for node in range(1, len(graph)):
        distance.append([inf for _ in range(len(graph))])
        estimate.append([inf for _ in range(len(graph))])
        message.append(set())

    for node in range(1, len(graph)):
        for neighbour, weight in graph[node]:
            estimate[neighbour][node] = weight
            message[neighbour].add((weight, node, node))
        distance[node][node] = 0


def compute_apsp(graph):
    distance, estimate, message = [None], [None], [None]
    initilisation(graph, distance, estimate, message)

    communication_rounds = 0
    best_message = [None for _ in range(len(graph))]
    for communication_round in range(2 * len(graph)):

        for node in range(1, len(graph)):
            best_message[node] = None

            while True:
                if not message[node]: break

                msg = min(message[node])
                message[node].discard(msg)

                value, source, _ = msg
                if distance[node][source] > value:
                    distance[node][source] = value
                    best_message[node] = msg
                    communication_rounds = communication_round + 1
                    break

        for node in range(1, len(graph)):
            if not best_message[node]: continue

            for neighbour, weight in graph[node]:
                value, source, sender = best_message[node]

                if neighbour == sender:
                    messages = [msg for msg in message[node] if msg[-1] != neighbour]
                    if not messages: continue
                    value, source, sender = min(messages)

                message[neighbour].add((value + weight, source, node))
                estimate[neighbour][source] = value + weight

    return distance, communication_rounds
