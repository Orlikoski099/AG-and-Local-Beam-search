import networkx as nx
import random

FILENAME = "D:/facul/SI/grafo.txt"

def read_graph_from_file():
    G = nx.Graph()
    with open(FILENAME, 'r') as file:
        for line in file:
            v1, v2, weight = map(int, line.strip().split(' '))
            G.add_edge(v1, v2, weight=weight)
    return G

def genetic_algorithm(graph, start_node, num_generations, population_size):
    # Criar população inicial aleatória
    population = [start_node] + random.sample(list(graph.nodes()), population_size-1)
    
    for generation in range(num_generations):
        # Avaliar a aptidão de cada indivíduo na população
        fitness_scores = [nx.shortest_path_length(graph, start_node, individual, weight='weight') for individual in population]
        
        # Selecionar os pais para reprodução por torneio
        parents = []
        for i in range(population_size//2):
            tournament = random.sample(range(population_size), k=2)
            if fitness_scores[tournament[0]] < fitness_scores[tournament[1]]:
                parents.extend([population[tournament[0]], population[tournament[1]]])
            else:
                parents.extend([population[tournament[1]], population[tournament[0]]])
        
        # Criar nova população a partir dos pais selecionados
        new_population = []
        for i in range(population_size//2):
            parent1, parent2 = parents[i*2], parents[i*2+1]
            crossover_point = random.randint(1, len(graph)-1)
            if crossover_point > 0:
                child = list(str(parent1))[:crossover_point] + list(str(parent2))[crossover_point:]
            else:
                child = list(str(parent2))            
            if child:
                mutation_point = min(random.randint(1, len(child)-1), len(child)-1)
            else:
                mutation_point = 0

            if mutation_point != 0 and mutation_point != crossover_point:
                child[mutation_point] = random.choice(list(graph.nodes()))

            new_population.append(child)
        
        # Substituir a população antiga pela nova população
        population = sorted(new_population, key=lambda individual: nx.shortest_path_length(graph, start_node, individual, weight='weight'))[:population_size]
    
    # Retornar o indivíduo mais apto na última geração
    return population[0]

genetic_algorithm(read_graph_from_file(), 9, 5, 15)