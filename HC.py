
#*************IMPORTANTE! Importaciones***************
from sys import maxsize 
from itertools import permutations
V = 4
 
# Problema del Viajero (Problema más común para este algoritmo) 
def travellingSalesmanProblem(graph, s): 
 
    # Administración de los vertices 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
    # Peso mínimo del ciclo Hamiltonian
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # Costo (peso)  del camino actual
        current_pathweight = 0
 
        # calcular el peso del camino actual 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # Actualizar valor mínimo 
        min_path = min(min_path, current_pathweight) 
         
    return min_path 
 
 
# Código del driver 
if __name__ == "__main__": 
 
    # Matriz del gráfo 
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
            [15, 35, 0, 30], [20, 25, 30, 0]] 
    s = 0
    print(f"El costo (peso) del camino mas corto es = {travellingSalesmanProblem(graph, s)}")