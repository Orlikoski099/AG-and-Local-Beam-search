import sys
import math
import time


def calculate_path_cost(G, path):
    cost = 0
    for i in range(len(path)-1):
        cost += G[path[i]][path[i+1]]
    return cost


def tsp_helper(current, visited, G, path=[], cost=0):
    if len(visited) == len(G):
        return path + [current], cost + G[path[-1]][current]

    cheapest_path = None
    cheapest_cost = float('inf')

    for neighbor in G[current]:
        if neighbor not in visited:
            new_visited = visited + [neighbor]
            new_path, new_cost = tsp_helper(neighbor, new_visited, G, path + [current], cost + G[current][neighbor])
            if new_cost < cheapest_cost:
                cheapest_path = new_path
                cheapest_cost = new_cost

    return cheapest_path, cheapest_cost


def tsp(start, G):
    visited = [start]
    path, cost = tsp_helper(start, visited, G)

    if path is None:
        return [], math.inf

    path.append(start)
    cost += G[path[1]][start]

    return path, cost


if __name__ == '__main__':
    filename = "grafo.txt"
    start = 8

    G = {}
    with open(filename) as f:
        for line in f:
            v1, v2, weight = map(int, line.strip().split())
            if v1 not in G:
                G[v1] = {}
            if v2 not in G:
                G[v2] = {}
            G[v1][v2] = weight
            G[v2][v1] = weight

    start_time = time.time()

    path, cost = tsp(start, G)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds") 
    print('Path:', path)
    print('Cost:', cost)
