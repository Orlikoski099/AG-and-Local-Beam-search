import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_weighted_graph(num_nodes, num_edges):
    # Cria um grafo vazio
    G = nx.Graph()

    # Adiciona os nós ao grafo
    nodes = range(num_nodes)
    G.add_nodes_from(nodes)

    # Adiciona as arestas ao grafo
    edges = []
    while len(edges) < num_edges:
        # Escolhe dois nós aleatórios
        node1, node2 = random.sample(nodes, 2)
        # Gera um peso aleatório para a aresta
        weight = random.randint(0, 10)
        # Adiciona a aresta ao grafo
        G.add_edge(node1, node2, weight=weight)
        edges.append((node1, node2))

    # Desenha o grafo com os pesos das arestas
    nx.write_edgelist(G, "grafo.txt", data=['weight'])


    # Salva a imagem do grafo em formato png
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.savefig("grafo.png")
    plt.show()

# Exemplo de uso
generate_random_weighted_graph(15, 300)
