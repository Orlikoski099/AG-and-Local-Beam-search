import networkx as nx

filename = "Z:\Facul\SI\grafo.txt"

def read_graph_from_file(filename):
    G = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            v1, v2, weight = map(int, line.strip().split(' '))
            G.add_edge(v1, v2, weight=weight)
    return G

def find_shortest_path_in_file_graph(filename, start_node, end_node):
    G = read_graph_from_file(filename)
    shortest_path, shortest_path_length = nx.dijkstra_path(G, start_node, end_node), nx.dijkstra_path_length(G, start_node, end_node)
    print("O caminho mínimo de {} para {} é: {}".format(start_node, end_node, shortest_path))
    print("O custo do caminho mínimo é: {}".format(shortest_path_length))

find_shortest_path_in_file_graph(filename, 96, 85)