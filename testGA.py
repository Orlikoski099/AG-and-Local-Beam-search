from contextlib import nullcontext
import random
import math
import networkx as nx
import time

FILENAME = "D:/facul/SI/kGrafo.txt"

MUTACAO = 70

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
    a = []
    if (type(son) != type(a)):
        seq = son.sequencia
    else:
        seq = son
    sizeMax =  len(seq)
    nums = list(range(0, sizeMax))
    random.shuffle(nums)
    swap1 = 0
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
    
    # Índices aleatórios para os elementos do meio dos vetores
    indices = random.sample(range(0, n), n-2)
    
    for i in range(0, n-1):
        if i in indices:
            # Se o índice foi selecionado aleatoriamente, mistura com o outro vetor
            if v1[i] not in mixed[:i]:
                mixed[i] = v1[i]
            elif v2[i] not in mixed[:i]:
                mixed[i] = v2[i]
            else:
                raise ValueError("Não foi possível misturar os vetores")
        else:
            # Se o índice não foi selecionado aleatoriamente, copia o valor de v1
            mixed[i] = v1[i]
    
    return mixed

def crossover(plebe):
    
    sequencias = []
    newPop = []
    
    for i in plebe:
        sequencias.append(i.sequencia)

    size = len(sequencias)

    for i in range(size):
        v1 = sequencias[random.randint(0, size-1)]
        v2 = sequencias[random.randint(0, size-1)]
        newSon = mix_vectors(v1, v2) 
        newPop.append(newSon)
        # print(newSon)

    return newPop

def newGen (final):
    newPop = []
    sizeFinal = len(final)
    mutations = 0
    # elite = 2
    elite = math.ceil((sizeFinal * 20)/100)

    if elite > 0:
        for i in range(elite):
            newPop.append(final[i].sequencia)
            final.remove(final[i])
    for i in final:
        if random.randint(1, 100) > MUTACAO:
            mutations += 1
            final.remove(i)
            i.sequencia = mutation(i)
            newPop.append(i.sequencia)

    newSons = crossover(final)

    # for i in newSons:
    #     if random.randint(1, 100) > MUTACAO:
    #         mutations += 1
    #         newSons.remove(i)
    #         i = mutation(i)
    #         newSons.append(i)

    for i in newSons:
        newPop.append(i)

    return newPop

def run(pop, gen):

    costHistory = []
    lastCost = -1

    populacao = []
    G = read_graph_from_file()

    vertices = list(G.nodes)

    for i in range(pop):
        solucao = vertices.copy()
        random.shuffle(solucao)
        # solucao.append(solucao[0])
        populacao.append(solucao)


    final_population = []

    for j in range(gen):
        print(f"Gen: {j}")
        final_population.clear()
        for i in populacao:
            custo = sequential_search(G, i[:len(i)-1])
            custo += nx.shortest_path_length(G, i[len(i)-1], 0, weight='weight')
            son = Son(i, custo)
            final_population.append(son)
                 

        ordenado = sorted(final_population, key=lambda son: son.custo)
        # for i in ordenado:
        #     print(i.custo)

        print(f"melhor custo da geração {j}: {ordenado[0].custo}")
        seqToShow = ordenado[0].sequencia
        print(f"melhor individuo da geração {j}: {seqToShow}")
        if ordenado[0].custo != lastCost:
            lastCost = ordenado[0].custo
            costHistory.append(lastCost)
        populacao = newGen(ordenado)

    print(f"As evoluções foram: {costHistory}")
    # print (sequential_search(G, final_population[3].sequencia))
    # print (final_population[1].sequencia)
    # print (final_population[2].sequencia)

startTime = time.time()
run(20, 1000)

print(time.time()-startTime)
