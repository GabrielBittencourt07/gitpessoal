
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
    lista_vertices = sorted(lista_vertices)

    #============ MATRIZ ADJACÊNCIA ============= 

    n = len(lista_vertices)
    matriz_adj = np.zeros((n, n))

    for v1, v2 in lista_arestas: 
        ind_v1 = lista_vertices.index(v1)
        ind_v2 = lista_vertices.index(v2)
        matriz_adj[ind_v1][ind_v2] += 1 
        matriz_adj[ind_v2][ind_v1] += 1
        


    #============ MATRIZ INCIDÊNCIA ============= 
    m = len(lista_arestas)
    matriz_inc = np.zeros((n, m))

    for aresta in lista_arestas: 
        ind_a = lista_arestas.index(aresta)
        for vertice in aresta: 
            ind_v = lista_vertices.index(vertice)
            matriz_inc[ind_v][ind_a] += 1 

    return (matriz_adj, matriz_inc)

def funcao_adj(matriz_adj: NDArray) -> Tuple[List, NDArray]:
    pass


def executar(objeto: List | NDArray):
    for i in objeto: 
        if isinstance(i, Tuple): #Verifica se é uma lista com as arestas do grafo. 
            return funcao_lista(objeto)

        elif isinstance(i, List): #Verifica se é uma Array(Matriz)
            matriz = np.array(objeto)
            n,m = matriz.shape

            if n != m: #Matriz retangular implica nela ser uma matriz de incidencia.
                return #funcao_inc(objeto)

            elif matriz == np.transpose(matriz): #Matriz de adjacencia necessariamente é simétrica (para grafos não direcionados).
                return #funcao_adj(objeto)
            else:
                return #funcao_inc(objeto)    

        else: 
            raise ValueError("Dado no formato inválido")
        

list = [(0,1), (2,4), (2,5), (1,2), (3,1), (3,4), (0,0), (3,5)]

print(executar(list))







