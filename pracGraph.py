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

# grafo = Graph(is_dir=True)

# def cargar_grafo(grafo):
#     # 1. Agregamos los vértices del grafo
#     nodos = ['A', 'B', 'C', 'D', 'E']
#     for nodo in nodos:
#         grafo.add_vertex(nodo)
        
#     # 2. Cargamos las aristas respetando el orden: (weight, origin, destination)
#     grafo.add_edge(4, 'A', 'B')
#     grafo.add_edge(2, 'A', 'C')
#     grafo.add_edge(5, 'A', 'E')
    
#     grafo.add_edge(1, 'B', 'C')
#     grafo.add_edge(6, 'B', 'E') # La arista larga que pasa por arriba
    
#     grafo.add_edge(1, 'C', 'B') # La vuelta de C a B
#     grafo.add_edge(3, 'C', 'D')
    
#     # grafo.add_edge(2, 'D', 'D') # El ciclo directo (bucle) en D (descomentar si lo pide la consigna)
    
#     grafo.add_edge(4, 'E', 'D')


# cargar_grafo(grafo)

# grafo.show()

# C

# min_tree = grafo.kruskal("C")

# print(min_tree)
# peso_total = 0
# for edge in min_tree.split(';'):
#     origin, destination, weight = edge.split('-')
#     print(f'origin {origin} destination {destination}')
#     peso_total += int(weight)

# print(f"\nEl peso total del Árbol de Expansión Mínima es: {peso_total}")




# D

# grafo.add_edge(2,"E","C")

# print()
# grafo.show()



# E


# exist_path = grafo.exist_path('A', 'D')

# if exist_path:
#     paths = grafo.dijkstra('A')#lugar del que parto

#     destination = 'D'#lugar al que quiero llegar

#     peso_total = None

#     camino_completo = []

#     while paths.size() > 0:
#         value = paths.pop()
#         if value[0] == destination:#evalua hasta llegar y despues vuelve en reversapor el camino
#             if peso_total is None:
#                 peso_total = value[1]  # Guarda el peso total acumulado
#             camino_completo.append(value[0])  # Agrega el nodo al camino
#             destination = value[2]  # Actualiza el destino al nodo anterior ("de dónde vino")
#     camino_completo.reverse()
#     print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')
    
    

# 3. Implementar un grafo no dirigido que permita cargar puertos y las aristas que conecten dichos puertos, que permita resolver las siguientes tareas:
# a. cada arista debe tener la distancia que separa dichos puertos;
# b. realizar un barrido en profundidad desde el primer puerto en el grafo;
# c. determinar el camino más corto desde puerto Madero al puerto de Rodas;
# d. determinar el puerto con mayor número de aristas y eliminarlo.

grafo = Graph(is_dir=False)


oringin = ["Puerto Madero", "Puerto de Rodas", "Puerto La Plata", "Mar del Plata"]

# Lista de aristas: (Origen, Destino, Distancia)
edges = [
    ("Puerto Madero", "Puerto La Plata", 50),
    ("Puerto La Plata", "Mar del Plata", 400),
    ("Puerto Madero", "Puerto de Rodas", 1200)
]


def cargar_grafo_aris(grafo : Graph , oringin : list  , edges : list):
    
    for ori in oringin:
        grafo.add_vertex(ori)
        
    
    for origen, destino, distancia in edges:
         grafo.add_edge(distancia, origen, destino)

cargar_grafo_aris(grafo,oringin,edges)

grafo.show()

print()

# B
grafo.deep_show("Puerto Madero")

print()

# C

exist_path = grafo.exist_path('Puerto Madero', 'Puerto de Rodas')

if exist_path:
    paths = grafo.dijkstra('Puerto Madero')#lugar del que parto

    destination = 'Puerto de Rodas'#lugar al que quiero llegar

    peso_total = None

    camino_completo = []

    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destination:#evalua hasta llegar y despues vuelve en reversapor el camino
            if peso_total is None:
                peso_total = value[1]  # Guarda el peso total acumulado
            camino_completo.append(value[0])  # Agrega el nodo al camino
            destination = value[2]  # Actualiza el destino al nodo anterior ("de dónde vino")
    camino_completo.reverse()
    print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')



# D


















