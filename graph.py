from typing import Any, Optional
from list_ import List
from queue import Queue
from stack import Stack
from heap import HeapMin
from random import randint



class Graph(List):


    class _nodeVertex():

        def __init__(self, value, other_values=None):
            self.value = value
            self.other_values = other_values
            self.edges = List()
            self.visited = False

            def _sort_by_destination(item):
                return item.destination

            self.edges.add_criterion('destination', _sort_by_destination)

        def __str__(self):
            return f"{self.value}"

    class _nodeEdge():

        def __init__(self, weight, destination):
            self.weight = weight
            self.destination = destination

        def __str__(self):
            return f"weight: {self.weight} -> destination: {self.destination}"

    def __init__(self, is_dir=True):
        self.is_dir = is_dir

        def sort_by_value(item):
            return item.value

        self.add_criterion('value', sort_by_value)


    def add_vertex(self, value: Any, other_values: Any = None) -> None:
        node_vertex = self._nodeVertex(value, other_values)
        self.append(node_vertex)

    def add_edge(self, weight: Any, origin: Any, destination: Any) -> None:

        pos_origin = self.search(origin, 'value')
        if pos_origin is None:
            print('no existe origien')
            return

        pos_destination = self.search(destination, 'value')
        if pos_destination is None:
            print('no existe el destino')
            return

        node_edge = self._nodeEdge(weight, destination)
        self[pos_origin].edges.append(node_edge)

        if origin != destination and not self.is_dir:
            node_edge = self._nodeEdge(weight, origin)
            self[pos_destination].edges.append(node_edge)

    def delete_vertex(self, value):
        result = self.delete_value(value, 'value')
        
        #limpiar aristas
        for vertex in self:
            # self.delete_edge(vertex.value, value)
            vertex.edges.delete_value(value, 'destination')
        
        return result

    def delete_edge(self, origin, destination) -> Optional[Any]:
        pos_origin = self.search(origin, 'value')
        if pos_origin is None:
            print('no existe origien')
            return

        result  = self[pos_origin].edges.delete_value(destination, 'destination')

        if not self.is_dir:
            pos_destination = self.search(destination, 'value')
            if pos_destination is not None:
                self[pos_destination].edges.delete_value(origin, 'destination')

        return result

    def show(self):
        for vertex in self:
            print(vertex)
            if len(vertex.edges) > 0:
                print('aristas ->')
                for edge in vertex.edges:
                    print(edge)

    def deep_show(self, origin) -> None:#barrido en profundidad

        def _deep_show(origin) -> None:
            pos_origin = self.search(origin, 'value')
            if pos_origin is not None:
                visited = self[pos_origin].visited
                if not visited:
                    self[pos_origin].visited = True
                    print(self[pos_origin].value)
                    edges = self[pos_origin].edges
                    for edge in edges:
                        _deep_show(edge.destination)

        for vertex in self:
            vertex.visited = False
        
        _deep_show(origin)

    def amplitude_show(self, origin) -> None:#hace un barrido ampio
        for vertex in self:
            vertex.visited = False
    
        pending_queue = Queue()
        pos_origin = self.search(origin, 'value')
        if pos_origin is not None:
            visited = self[pos_origin].visited
            if not visited:
                pending_queue.arrive(self[pos_origin])
                while pending_queue.size() > 0:
                    # print()
                    # pending_queue.show()
                    # input()
                    # print()
                    vertex = pending_queue.attention()
                    if not vertex.visited:
                        vertex.visited = True
                        print(vertex.value)
                        edges = vertex.edges
                        for edge in edges:
                            # print(edge.destination)
                            pos_next_vertex = self.search(edge.destination, 'value')
                            pending_queue.arrive(self[pos_next_vertex])

    def dijkstra(self, origin):
        from math import inf
        
        no_visited = HeapMin()
        path = Stack()
        
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)

        while no_visited.size() > 0:
            # for element in no_visited.elements:
            #     print(element)
            # print()
            # input()
            vertex = no_visited.attention()
            costo_nodo_actual = vertex[0]
            path.push([vertex[1][0], costo_nodo_actual, vertex[1][2]])
            edges = vertex[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.destination)
                if pos is not None:
                    if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = vertex[1][0]
                        no_visited.elements[pos][0] = costo_nodo_actual + edge.weight
                        no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path                    


    def kruskal(self, origin_vertex):#expansion minima
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = []#agrega los vertices
        edges = HeapMin()
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.destination], edge.weight)#value es el origen

        print(forest)
        for element in edges.elements:
            print(element )
        
        while len(forest) > 1 and edges.size() > 0:
            edge = edges.attention()# devuelve el primero de la tabla
            origin = search_in_forest(forest, edge[1][0])# vertice del origen vertex.value/busca en el bosque
            destination = search_in_forest(forest, edge[1][1])# vertice destino edge.destination
            if origin is not None and destination is not None:
                if origin != destination:# compara si estan en dististas islas [A,B].A es el origen y B el destino
                    if origin > destination:
                        vertex_origin = forest.pop(origin)#saca los valores 
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)


                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        from_vertex = search_in_forest(forest, origin_vertex)#llama para ver en que posicion quedo el nodo que llame
        
        return forest[from_vertex] if from_vertex is not None else forest


    def exist_path(self, origin, destination):
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.destination, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result

        for vertex in self:
            vertex.visited = False

        result = __exist_path(self, origin, destination)
        return result

    # ejercicio de practica punto 1
    
    def cargar_grafo(self):
        # Usamos un while para garantizar que sean exactamente 15 vértices únicos
        while len(self) < 15:
            vertice = randint(1, 100)
            # Verificamos que no exista previamente en el grafo
            if self.search(vertice, 'value') is None:
                self.add_vertex(vertice)

    def cargar_aristas(self):
        aristas_creadas = set()  # Usamos un conjunto para evitar aristas repetidas
        
        while len(aristas_creadas) < 30:
            # Seleccionamos un origen y un destino aleatorios de los vértices existentes
            origen = self[randint(0, len(self) - 1)].value
            destino = self[randint(0, len(self) - 1)].value
            
            # Controlamos que la arista (origen -> destino) no haya sido creada antes
            if (origen, destino) not in aristas_creadas:
                aristas_creadas.add((origen, destino))
                peso = randint(1, 100)
                self.add_edge(peso, origen, destino)

    
    #A
    def delete_sin_aristas(self):
        aux = []
        cont = 0
        for vertex in self:
            if len(vertex.edges) == 0:
                aux.append(vertex.value)
        for value in aux:
            self.delete_vertex(value)
            cont+=1

        return cont
    
    
    #B
    def nodos_mayor_aristas_salida(self):
        max_aristas = 0
        nodos_max = []
    
        for vertice in self :
            cantidad_aristas = len(vertice.edges)
            if cantidad_aristas > max_aristas:
                max_aristas = cantidad_aristas
                nodos_max = [vertice.value]
            elif cantidad_aristas == max_aristas:
                nodos_max.append(vertice.value)
    
        return nodos_max, max_aristas
    
    #c
    def nodos_mayor_aristas_llegada(self):
        max_aristas = 0
        nodos_max = []
    
        for vertice in self:
            contador = 0
            # Buscamos en todo el grafo cuántas veces apunta hacia este vértice
            for v in self:
                for edge in v.edges:
                    if edge.destination == vertice.value:
                        contador += 1
        
            # Aplicamos exactamente tu misma lógica de comparación
            if contador > max_aristas:
                max_aristas = contador
                nodos_max = [vertice.value]
            elif contador == max_aristas:
                nodos_max.append(vertice.value)
            
        return nodos_max, max_aristas
    
    #D
    
    def nodos_sin_aristas_llegada(self):
        # Recolectamos todos los destinos que sí reciben al menos una arista
        destinos_con_llegada = set()
        for vertice in self:
            for edge in vertice.edges:
                destinos_con_llegada.add(edge.destination)
            
        # Buscamos qué vértices del grafo NO están en ese conjunto de llegadas
        nodos_aislados_llegada = List()
        for vertice in self:
            if vertice.value not in destinos_con_llegada:
                nodos_aislados_llegada.append(vertice.value)
            
        return nodos_aislados_llegada


    #E
    def cont_vert(self):
        cont = 0
    
        for vertex in self:
            if vertex is not None:
                cont += 1
    
        return cont
    
    #F
    
    def vertices_con_ciclo_directo(self):
        contador_vertices = 0
        verte = []
        for vertex in self:
            # Revisamos cada arista que SALE de este vértice
            tiene_lazo = False
            for edge in vertex.edges:
                # Si el destino de la arista es igual al valor del propio vértice, hay un ciclo directo
                if edge.destination == vertex.value:
                    verte.append(vertex.value)
                    break # Con que encontremos uno, ya sabemos que este vértice cumple
            
            contador_vertices = len(verte)
                
        return verte , contador_vertices
    
    #G
    
    def arista_mas_larga(self):
        max_peso = None
        aristas_max = []
        
        for vertex in self:
            for edge in vertex.edges:
                # Si es la primera arista que vemos o encontramos una con mayor peso
                if max_peso is None or edge.weight > max_peso:
                    max_peso = edge.weight
                    # Guardamos una tupla con (origen, destino, peso)
                    aristas_max = [(vertex.value, edge.destination, edge.weight)]
                # Si empata con el peso máximo actual, la agregamos a la lista
                elif edge.weight == max_peso:
                    aristas_max.append((vertex.value, edge.destination, edge.weight))
                    
        return aristas_max, max_peso
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    