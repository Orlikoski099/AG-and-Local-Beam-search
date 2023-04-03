import networkx as nx
import matplotlib.pyplot as plt
import random

n = 30  # Número de vértices
G = nx.DiGraph(nx.complete_graph(n).to_directed())

def showGraph():

    nx.write_edgelist(G, "kGrafo.txt", data=['weight'])

    # Salva a imagem do grafo em formato png
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.savefig("kGrafo.png")
    # plt.show()


# Atribuindo pesos aleatórios às arestas
for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 500)

showGraph()