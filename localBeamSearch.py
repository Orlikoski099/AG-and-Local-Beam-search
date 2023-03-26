import random

def local_search(initial_solution, generate_neighbors, evaluate_solution, max_iterations):
    """
    Algoritmo de busca local que busca uma solução ótima próxima à solução inicial.
    
    Args:
        initial_solution (Any): Solução inicial do problema.
        generate_neighbors (function): Função que gera vizinhos a partir de uma solução.
        evaluate_solution (function): Função que avalia a qualidade de uma solução.
        max_iterations (int): Número máximo de iterações.
        
    Returns:
        Any: Solução ótima encontrada.
    """
    current_solution = initial_solution
    
    for i in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        best_neighbor = max(neighbors, key=evaluate_solution)
        
        if evaluate_solution(best_neighbor) > evaluate_solution(current_solution):
            current_solution = best_neighbor
        else:
            break
        
    return current_solution
