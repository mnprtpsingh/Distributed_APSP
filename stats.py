import random
import matplotlib.pyplot as plt

from utils import create_graph
from floyd_warshall import get_apsp
from distributed_apsp import compute_apsp


def get_stats():
    iterations, max_nodes = 10000, 64
    stats = {}

    for _ in range(iterations):
        graph = create_graph(max_nodes)
        number_of_nodes = len(graph) - 1

        actual_apsp = get_apsp(graph)
        computed_apsp, communication_rounds = compute_apsp(graph)
        assert actual_apsp == computed_apsp

        ratio = round(communication_rounds / number_of_nodes, 1)
        if ratio in stats: stats[ratio] += 1
        else: stats[ratio] = 1

    for key in stats:
        stats[key] = round(stats[key] / iterations, 6)

    return stats


def display_stats():
    stats = get_stats()
    idx, height = list(stats.keys()), list(stats.values())

    plt.figure(figsize=(12, 4))
    plt.bar(idx, height, width=0.05)
    plt.xticks(idx)

    plt.title("Execution of Distributed APSP 10000 times \n on Different Randomly Created Graphs")
    plt.xlabel('Ratio of Communication Rounds Required and Number of Nodes')
    plt.ylabel('Frequency (per 10000)')

    for idx, height in stats.items():
        plt.text(idx - 0.04, height + 0.005, '{:.4f}'.format(height))

    plt.show()


if __name__ == "__main__":
    random.seed(0)
    display_stats()
