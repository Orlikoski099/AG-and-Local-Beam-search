import random
import math
import networkx as nx
import time

FILENAME = "Z:\Facul\SI\local-beam-search\kGrafo.txt"

MUTACAO = 60



class Son:
    def __init__(self, sequencia, custo):
        self.sequencia = sequencia
        self.custo = custo

def read_graph_from_file():
    with open(FILENAME) as file:
        lines = file.readlines()
        edges = [tuple(map(int, line.split())) for line in lines]
    G = nx.DiGraph()
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    return G
    
def sequential_search(graph, vertices):
    total_weight = 0
    current_node = vertices[0]
    for i in range(len(vertices) - 1):
        current_node = vertices[i]
        next_node = vertices[i + 1]
        if current_node != next_node:
            if not graph.has_edge(current_node, next_node):
                print(f"A aresta {current_node} -> {next_node} não existe no grafo.")
                return None
            path = nx.shortest_path_length(graph, current_node, next_node, weight='weight')
            total_weight += path
        else:
            pass

    return total_weight

def mutation(son):
    seq = son.sequencia
    sizeMax =  len(seq)-1
    nums = list(range(1, sizeMax))
    random.shuffle(nums)
    swap1 = nums[0]
    swap2 = nums[1]

    aux = seq[swap1]
    seq[swap1] = seq[swap2]
    seq[swap2] = aux

    return seq

def mix_vectors(v1, v2):
    n = len(v1)
    assert n == len(v2), "Os vetores devem ter o mesmo tamanho"
    
    mixed = [0] * n
    
    mixed[0] = v1[0]
    
    mixed[n-1] = v1[n-1]
    
    for i in range(1, n-1):
        if v1[i] not in mixed[:i]:
            mixed[i] = v1[i]
        elif v2[i] not in mixed[:i]:
            mixed[i] = v2[i]
        else:
            raise ValueError("Não foi possível misturar os vetores")
    
    return mixed

def crossover(plebe):
    
    sequencias = []
    newPop = []
    
    for i in plebe:
        sequencias.append(i.sequencia)

    size = len(sequencias)

    for i in range(size):
        newPop.append(mix_vectors(sequencias[random.randint(0, size-1)], sequencias[random.randint(0, size-1)]))

    return newPop

def newGen (final):
    newPop = []
    sizeFinal = len(final)
    mutations = 0
    elite = math.ceil((sizeFinal * 20)/100)

    for i in range(elite):
        newPop.append(final[i].sequencia)
        final.remove(final[i])
    for i in final:
        if random.randint(1, 100) > MUTACAO:
            mutations += 1
            i.sequencia = mutation(i)
            newPop.append(i.sequencia)
            final.remove(i)

    newSons = crossover(final)

    for i in newSons:
        newPop.append(i)

    return newPop

def run(pop, gen):

    populacao = []
    G = read_graph_from_file()

    vertices = list(G.nodes)

    for i in range(pop):
        solucao = vertices.copy()
        random.shuffle(solucao)
        solucao.append(solucao[0])
        populacao.append(solucao)


    final_population = []

    for j in range(gen):
        print(f"Gen: {j}")
        final_population.clear()
        for i in populacao:
            custo = sequential_search(G, i)
            son = Son(i, custo)
            final_population.append(son)
                 

        ordenado = sorted(final_population, key=lambda son: son.custo)
        print(f"melhor custo da geração {j}: {ordenado[0].custo}")
        populacao = newGen(ordenado)

    print (populacao[0])
    print(len(populacao))

startTime = time.time()
run(10, 20)

print(time.time()-startTime)