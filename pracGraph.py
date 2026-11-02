
from heap import HeapMin
from graph import Graph
from random import randint
from list_ import List
from stack import Stack
from queue import Queue

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

# grafo.show()

# print()

# # B
# grafo.deep_show("Puerto Madero")

# print()

# # C

# grafo.devolver_camino("Puerto Madero", "Puerto de Rodas")


# D

# aristas_max_llegada = grafo.nodos_mayor_aristas_llegada()

# if len(aristas_max_llegada) > 0:
#     print(f"Los nodos con mayor cantidad de aristas de llegada son: {aristas_max_llegada}")
    
#     # Eliminamos cada uno de los nodos
#     for nodo in aristas_max_llegada:
#         grafo.delete_vertex(nodo)
        
#     # Mensaje de confirmación fuera de condiciones innecesarias
#     print("Se eliminaron los vértices correctamente.") 
# else:
#     print("No hay nodos con aristas de llegada.")
    



# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación:

# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido.

grafo = Graph(is_dir=True)


vertices = {
    # Routers
    "Router 1": "router",
    "Router 2": "router",
    "Router 3": "router",
    
    # Switches
    "Switch 1": "switch",
    "Switch 2": "switch",
    
    # Servidores
    "Guarani": "servidor",
    "MongoDB": "servidor",
    
    # Impresora
    "Impresora": "impresora",
    
    # Notebooks (triángulos azules)
    "Red Hat": "notebook",
    "Debian": "notebook",
    "Arch": "notebook",
    
    # PCs (cuadrados amarillos)
    "Ubuntu": "pc",
    "Mint": "pc",
    "Manjaro": "pc",
    "Fedora": "pc",
    "Parrot": "pc"
}

aristas_completo = [
    # Router 2
    ("Router 2", "Red Hat", 25),
    ("Router 2", "Guarani", 9),
    ("Router 2", "Router 3", 50),
    ("Router 2", "Router 1", 37),
    
    # Router 1
    ("Router 1", "Router 3", 43),
    ("Router 1", "Switch 1", 29),
    
    # Switch 1 y sus dispositivos
    ("Switch 1", "Debian", 17),
    ("Switch 1", "Ubuntu", 18),
    ("Switch 1", "Impresora", 22),
    ("Switch 1", "Mint", 80),
    
    # Router 3 hacia Switch 2
    ("Router 3", "Switch 2", 61),
    
    # Switch 2 y sus dispositivos / conexiones
    ("Switch 2", "Manjaro", 40),
    ("Switch 2", "Fedora", 3),
    ("Switch 2", "Parrot", 12),
    ("Switch 2", "MongoDB", 5),
   
    ("Switch 2", "Arch", 56)
]

# A
def cargar_grafo(grafo: Graph, vertices):
    for nombre, tipo in vertices.items():
        grafo.add_vertex(nombre , tipo)


cargar_grafo(grafo, vertices)

def cargar_aristas(grafo: Graph, aristas_completo):
    for origen, destino, peso in aristas_completo:
        grafo.add_edge(peso, origen, destino)

cargar_aristas(grafo, aristas_completo)

# grafo.show()

#B
# print("Barrido en profundidad desde Red Hat:")
# grafo.deep_show("Red Hat")
# print("\nBarrido en profundidad desde Debian:")
# grafo.deep_show("Debian")

# print("\nBarrido en profundidad desde Arch:")
# grafo.deep_show("Arch") 
# print("\nBarrido en amplitud desde Red Hat:")
# grafo.amplitude_show("Red Hat")

# print("\nBarrido en amplitud desde Debian:")
# grafo.amplitude_show("Debian")  
# print("\nBarrido en amplitud desde Arch:")
# grafo.amplitude_show("Arch")




# C //desde la pc: Manjaro,Red Hat, Fedora hasta la impresora;
    

# --- EJECUCIÓN DIRECTA DEL PUNTO C ---
# print("\nCaminos más cortos hasta la impresora:")

# grafo.devolver_camino("Red Hat","Impresora")
# grafo.devolver_camino("Manjaro","Impresora")
# grafo.devolver_camino("Fedora","Impresora")


# D

# grafo.espansion_min("Impresora")

# E

# grafo.devolver_camino("Manjaro","Guarani")


# F

# grafo.devolver_camino("Switch 1","MongoDB")

# G

# grafo.delete_edge('Switch 1', 'Impresora')
# grafo.add_edge(6, 'Router 2', 'Impresora')
# print()


# print("Barrido en profundidad desde Red Hat:")
# grafo.deep_show("Red Hat")
# print("\nBarrido en profundidad desde Debian:")
# grafo.deep_show("Debian")

# print("\nBarrido en profundidad desde Arch:")
# grafo.deep_show("Arch") 
# print("\nBarrido en amplitud desde Red Hat:")
# grafo.amplitude_show("Red Hat")

# print("\nBarrido en amplitud desde Debian:")
# grafo.amplitude_show("Debian")  
# print("\nBarrido en amplitud desde Arch:")
# grafo.amplitude_show("Arch")


# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.


g = Graph(is_dir = False)

# A

g.add_vertex("cocina", None)
g.add_vertex("comedor", None)
g.add_vertex("cochera", None)
g.add_vertex("baño 1", None)
g.add_vertex("baño 2", None)
g.add_vertex("habitacion 1", None)
g.add_vertex("habitacion 2", None)
g.add_vertex("sala de estar", None)
g.add_vertex("terraza", None)
g.add_vertex("patio", None)

# B

g.add_edge(3, "cocina", "comedor") 
g.add_edge(32, "cocina", "cochera") 
g.add_edge(19, "cocina", "quincho") 
g.add_edge(5, "cocina", "habitación 2") 
g.add_edge(8, "cocina", "terraza") 
g.add_edge(2, "comedor", "baño 1") 
g.add_edge(1, "comedor", "patio") 
g.add_edge(15, "cochera", "sala de estar") 
g.add_edge(9, "cochera", "baño 2") 
g.add_edge(22, "quincho", "habitación 1") 
g.add_edge(14, "quincho", "terraza") 
g.add_edge(13, "quincho", "baño 2") 
g.add_edge(18, "quincho", "baño 1") 
g.add_edge(24, "habitación 1", "terraza") 
g.add_edge(29, "habitación 1", "patio") 
g.add_edge(21, "habitación 2", "sala de estar") 
g.add_edge(6, "habitación 2", "patio") 
g.add_edge(11, "baño 1", "sala de estar") 
g.add_edge(25, "baño 1", "patio") 
g.add_edge(20, "baño 1", "comedor") 
g.add_edge(4, "baño 2", "comedor") 
g.add_edge(10, "terraza", "comedor") 
g.add_edge(12, "terraza", "baño 1") 
g.add_edge(20, "terraza", "patio") 
g.add_edge(5, "patio", "comedor") 
g.add_edge(15, "patio", "baño") 
g.add_edge(10, "patio", "sala de estar") 
g.add_edge(5, "sala de estar", "comedor") 
g.add_edge(15, "sala de estar", "patio") 
g.add_edge(11, "sala de estar", "baño 1") 



#g.show()

# C

#g.espansion_min("patio")



# D

g.devolver_camino("habitación 1","sala de estar")






































