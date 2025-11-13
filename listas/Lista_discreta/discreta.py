
import numpy as np
from numpy.typing import NDArray
from typing import Tuple, List, overload


@overload
def executar(objeto: List)-> Tuple[NDArray, NDArray]: ...
@overload
def executar(objeto: NDArray)-> Tuple[List, NDArray]: ...

def funcao_lista(lista_arestas: List) -> Tuple[NDArray, NDArray]: 
    lista_vertices = []
    for v1, v2 in lista_arestas: 
        if v1 not in lista_vertices:
            lista_vertices.append(v1)
        if v2 not in lista_vertices: 
            lista_vertices.append(v2)
            

    #============ MATRIZ ADJACÊNCIA ============= 

    matriz_adj = np.zeros((len(lista_vertices), len(lista_vertices)))

    for v1, v2 in lista_arestas: 
        ind_v1 = lista_vertices.index(v1)
        ind_v2 = lista_vertices.index(v2)
        matriz_adj[ind_v1][ind_v2] += 1 
        
        if v1 == v2: 
            matriz_adj[ind_v1][ind_v2] += 1 

    #============ MATRIZ INCIDÊNCIA ============= 

    matriz_inc = np.zeros((len(lista_vertices), len(lista_arestas)))

    for aresta in lista_arestas: 
        ind_a = lista_arestas.index(aresta)
        for vertice in aresta: 
            ind_v = lista_vertices.index(vertice)
            matriz_inc[ind_v][ind_a] += 1 

    return matriz_adj, matriz_inc



def executar(objeto: List | NDArray):
    for i in objeto: 
        if isinstance(i, tuple): #Verifica se é uma lista com as arestas do grafo. 
            pass


        elif isinstance(i, List): #Verifica se é uma Array(Matriz).
            for j in i: 
                if isinstance(j, int): #Verifica se é uma Matriz de 
                    pass

            pass
        else: 
            raise ValueError("Dado no formato inválido")
        

list = [(0,1), (2,4), (2,5), (1,2), (3,1), (3,4), (3,1), (0,0), (3,5)]

print(funcao_lista(list))







