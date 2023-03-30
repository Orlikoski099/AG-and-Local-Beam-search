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
        
        # Selecionar os indivíduos mais aptos para reprodução
        selected_parents = random.choices(population, weights=fitness_scores, k=population_size//2)
        
        # Criar nova população a partir dos pais selecionados
        new_population = selected_parents.copy()
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_parents, 2)
            crossover_point = random.randint(1, len(start_node)-1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            mutation_point = random.randint(0, len(child)-1)
            child[mutation_point] = random.choice(list(graph.nodes()))
            new_population.append(child)
        
        # Substituir a população antiga pela nova população
        population = new_population
    
    # Retornar o indivíduo mais apto na última geração
    return min(population, key=lambda individual: nx.shortest_path_length(graph, start_node, individual, weight='weight'))

genetic_algorithm(read_graph_from_file(), 9, 5, 15)