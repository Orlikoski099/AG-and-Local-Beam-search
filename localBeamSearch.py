import random
import time
import networkx as nx
from queue import PriorityQueue

FILENAME = "D:/facul/SI/kGrafo.txt"

startTime = time.time()

def read_graph_from_file():
    with open(FILENAME) as file:
        lines = file.readlines()
        edges = [tuple(map(int, line.split())) for line in lines]
    G = nx.DiGraph()
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    return G
    

G = read_graph_from_file()

start_city = random.randint(0, len(G.nodes))
order = [start_city]
remaining_cities = list(range(len(G.nodes)))
remaining_cities.remove(start_city)

while len(remaining_cities) > 0:
    next_city = min(remaining_cities, key=lambda x: G.get_edge_data(order[-1], x)['weight'])
    order.append(next_city)
    remaining_cities.remove(next_city)


def beam_search(graph, order, beam_width):
    visited = []
    queue = PriorityQueue()
    queue.put((evaluate_order(order, graph), order))
    costs = [evaluate_order(order, graph)]
    while not queue.empty():
        queue_items = []
        while len(queue_items) < beam_width and not queue.empty():
            queue_items.append(queue.get())
        paths = [item[1] for item in queue_items]
        visited += [p[-1] for p in paths]

        new_costs = []
        for i, path in enumerate(paths):
            if len(path) == len(graph.nodes):
                return path, costs[i]

            for neighbor in graph.neighbors(path[-1]):
                if neighbor not in visited:
                    new_order = path + [neighbor]
                    new_cost = evaluate_order(new_order, graph)
                    new_costs.append(new_cost)
                    queue.put((new_cost, new_order))

        costs = new_costs

    return None, None


def evaluate_order(order, graph):
    total_distance = 0

    for i in range(len(order) - 1):
        total_distance += graph.get_edge_data(order[i], order[i+1])['weight']

    total_distance += graph.get_edge_data(order[-1], order[0])['weight']

    return total_distance





path = beam_search(G, order, 10)


print(f"Tempo decorrido: {time.time() - startTime}")
print(path)
