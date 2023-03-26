from grafo import list
import heapq

teste = list(5)

teste.readFile()

teste.printFile()


def dijkstra(graph, start):
    cost = {node: float('inf') for node in graph}
    cost[start] = 0
    pq = [(0, start)]
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if current_cost > cost[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            new_cost = cost[current_node] + weight
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return cost


dijkstra()
