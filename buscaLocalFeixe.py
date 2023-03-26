from grafo import list
import heapq

teste = list(5)

teste.readFile()

teste.printFile()


def dijkstra(graph, start):
    # Cria um dicionário para armazenar o custo mínimo de cada nó
    cost = {node: float('inf') for node in graph}
    # Define o custo inicial para o nó de partida como 0
    cost[start] = 0
    # Cria um heap de prioridade para selecionar o nó com o menor custo
    pq = [(0, start)]
    while pq:
        # Seleciona o nó com o menor custo
        current_cost, current_node = heapq.heappop(pq)
        # Se o custo atual for maior do que o custo armazenado, ignore este nó
        if current_cost > cost[current_node]:
            continue
        # Para cada vizinho do nó atual, calcula o custo do caminho até ele
        for neighbor, weight in graph[current_node].items():
            new_cost = cost[current_node] + weight
            # Se o novo custo for menor do que o custo armazenado, atualize o custo e adicione o vizinho ao heap de prioridade
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return cost
