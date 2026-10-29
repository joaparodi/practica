from graph import Graph
from random import randint
from list_ import List

# ejercicio de practica

# 1. Generar un grafo con 15 vértices aleatorios no repetidos (con números de 1 a 100), luego agregar
# 30 aristas –no repetidas– que conecten vértices de manera aleatoria, con etiquetas –también
# aleatorias– dentro del rango de 1 a 100, después resolver las siguientes actividades:
# a. primero eliminar los vértices que hayan quedado desconectados, es decir, que ningún otro
# vértice tenga una arista que lo apunte y que de él no salga ninguna arista;
# b. determinar el nodo con mayor cantidad de aristas que salen de él, puede ser más de uno;
# c. determinar el nodo con mayor cantidad de aristas que llegan a él, puede ser más de uno;
# d. indicar los vértices desde los cuales no se puede acceder a otro vértice;

# e. contar cuantos vértice componen el grafo, dado que se genera aleatoriamente y se elimi-
# nan los vértices que quedan desconectados;

# f. determinar cuántos vértices tienen un arista a sí mismo, es decir, un ciclo directo;
# g. determinar la arista más larga, indicando su origen, destino y valor –puede ser más de una.


# grafo = Graph(is_dir=True)

#cargar el grafo con vértices y aristas
# grafo.cargar_grafo()
# grafo.cargar_aristas()

# grafo.show()

# A

# aux = grafo.delete_sin_aristas()
# if aux is not None:
#     print(f"Se eliminaron {aux} vértices desconectados.")
# else:
#     print("No se eliminaron vértices desconectados.")
    
    
# B


# nodos_max_salida, cantidad_max_salida = grafo.nodos_mayor_aristas_salida()
# if cantidad_max_salida > 0:
#     print(f"Los nodos con mayor cantidad de aristas de salida ({cantidad_max_salida}) son: {nodos_max_salida}")
# else:
#     print("No hay nodos con aristas de salida.")
    

#c

# grafo.nodos_mayor_aristas_llegada()

# aristas_max_llegada, cantidad_max_llegada = grafo.nodos_mayor_aristas_llegada()
# if cantidad_max_llegada > 0:
#     print(f"Los nodos con mayor cantidad de aristas de llegada ({cantidad_max_llegada}) son: {aristas_max_llegada}")
# else:
#     print("No hay nodos con aristas de llegada.")
    

# D 


print()

# sin_llegadas = grafo.nodos_sin_aristas_llegada()
# if sin_llegadas.size() > 0 :
#     print(f"Vértices a los cuales no llega ninguna arista: {sin_llegadas}")
# else:
#     print("no se enconto ninguna")
    
#E

# cantidad_vertice = grafo.cont_vert()
# if cantidad_vertice is not None:
#     print(f"la cantidad de vertices es de :{cantidad_vertice}")
# else:
#     print("no tiene vertices")

# F

# vert, reflexivo = grafo.vertices_con_ciclo_directo()
# if reflexivo is not None:
#     print(f"las vertice que son reflexiva son en total: {reflexivo} y son: {vert}")
# else:
#     print("no hay ningun vertice que sea reflexivo")



# G

# mas_larga, max_peso = grafo.arista_mas_larga()

# if max_peso is not None:
#     print(f"La o las aristas más largas tienen un peso de {max_peso}:")
#     for origen, destino, peso in mas_larga:
#         print(f" - Desde el nodo {origen} hacia el nodo {destino}")
# else:
#     print("El grafo no tiene aristas.")






# 2. Sobre el siguiente dígrafo implementar los algoritmos necesarios para resolver las tareas que
# se presentan a continuación:
# a. represéntelo como arreglo de listas de adyacencias y lista de listas de adyacencia;
# b. cargue el valor de las etiquetas de todas las aristas;
# c. encuentre el árbol de expansión mínima, para este punto considere el grafo como no dirigido;
# d. agregue un arco de E hasta C;
# e. encuentre el camino más corto de A hasta D.

grafo = Graph(is_dir=True)

def cargar_grafo(grafo):
    # 1. Agregamos los vértices del grafo
    nodos = ['A', 'B', 'C', 'D', 'E']
    for nodo in nodos:
        grafo.add_vertex(nodo)
        
    # 2. Cargamos las aristas respetando el orden: (weight, origin, destination)
    grafo.add_edge(4, 'A', 'B')
    grafo.add_edge(2, 'A', 'C')
    grafo.add_edge(5, 'A', 'E')
    
    grafo.add_edge(1, 'B', 'C')
    grafo.add_edge(6, 'B', 'E') # La arista larga que pasa por arriba
    
    grafo.add_edge(1, 'C', 'B') # La vuelta de C a B
    grafo.add_edge(3, 'C', 'D')
    
    # grafo.add_edge(2, 'D', 'D') # El ciclo directo (bucle) en D (descomentar si lo pide la consigna)
    
    grafo.add_edge(4, 'E', 'D')


cargar_grafo(grafo)

grafo.show()

# C

min_tree = grafo.kruskal("A")

print(min_tree)
peso_total = 0
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)

print(f"\nEl peso total del Árbol de Expansión Mínima es: {peso_total}")




