from heap import HeapMin
from tree import BinaryTree
from random import randint
from queue import Queue
from tree import Node

# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria– que resuelva las siguientes actividades:
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

# arbol = BinaryTree()

# def cargar_arbol(arbol : BinaryTree):
#     for i in range(10):
#         arbol.insert_node(randint(0,20),None)


# cargar_arbol(arbol)
# # a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# print("arbol con barrido Preorden")
# arbol.preorden()
# print()
# print("arbol con barrido Inorden")
# arbol.inorden()
# print()
# print("arbol con barrido Postorden")
# arbol.postorden()
# print()
# print("arbol con barrido Por Nivel")
# print("falta implementar barrido por nivel")

# print()
# # b. determinar si un número está cargado en el árbol o no;

# print("determinar si un número está cargado en el árbol o no")
# print()
# arbol.search(2)
# aux = arbol.search(2)
# if aux is not None:
#     print(f"el valor {aux.value} se encuentra en el arbol")
# else:
#     print("el valor no se encuentra en el arbol")

# print()

# # c. eliminar tres valores del árbol;

# print("eliminar tres valores del árbol")

# print('eliminar', arbol.delete_node(20))
# arbol.preorden()
# print()
# print('eliminar', arbol.delete_node(10))
# arbol.preorden()
# print()
# print('eliminar', arbol.delete_node(5))
# arbol.preorden()
# print()


# # d. determinar la altura del subárbol izquierdo y del subárbol derecho;


# def altura_subarboles(arbol: BinaryTree, value):
#     def __altura(nodo):
#         if nodo is None:
#             return None
#         alt_izq = __altura(nodo.left)
#         alt_der = __altura(nodo.right)
        
#         izq = alt_izq if alt_izq is not None else -1
#         der = alt_der if alt_der is not None else -1
#         return 1 + max(izq, der)

#     aux = None
#     if arbol.root is None:
#         return None, None
#     else:
#         aux = arbol.search(value)
#         if aux is not None:
#             alt_izq = __altura(aux.left) if aux.left is not None else None
#             alt_der = __altura(aux.right) if aux.right is not None else None
#             return alt_izq, alt_der

#     return None, None

# print()
# # Ejecución de prueba del punto d
# print("Determinar la altura del subárbol izquierdo y derecho:")
# if arbol.root is not None:
#     valor_buscar = arbol.root.value  # Buscamos las alturas tomando como referencia la raíz actual
#     izq, der = altura_subarboles(arbol, valor_buscar)
#     print(f"Subárboles del nodo {valor_buscar} = Izquierdo: {izq} | Derecho: {der}")
# print()


# # e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# def contar_ocurrencias(arbol: BinaryTree):
#     def __contar(root, acumulador):
#         # 1. Sumamos 1 por el nodo actual en el que estamos parados
#         acumulador += 1

#         # 2. Va hacia el subárbol izquierdo actualizando el acumulador
#         if root.left is not None:
#             acumulador = __contar(root.left, acumulador)

#         # 3. Vuelve al tronco y va hacia el subárbol derecho acumulando el resultado
#         if root.right is not None:
#             acumulador = __contar(root.right, acumulador)

#         return acumulador

#     if arbol.root is None:
#         return 0

#     # Inicia desde el tronco (raíz) mandando el acumulador en 0
#     return __contar(arbol.root, 0)


# total = contar_ocurrencias(arbol)
# print(f"Total de nodos en el árbol: {total}")


# print()

# # f. contar cuántos números pares e impares hay en el árbol.
# def contar_pares_impares(arbol: BinaryTree):
#     def __contar(root, pares, impares):
#         # 1. Incrementamos el acumulador correspondiente según el nodo actual
#         if root.value % 2 == 0:
#             pares += 1
#         else:
#             impares += 1

#         # 2. Recorremos el subárbol izquierdo actualizando ambos acumuladores
#         if root.left is not None:
#             pares, impares = __contar(root.left, pares, impares)

#         # 3. Volvemos al tronco y recorremos el subárbol derecho
#         if root.right is not None:
#             pares, impares = __contar(root.right, pares, impares)

#         return pares, impares

#     if arbol.root is None:
#         return 0, 0

#     # Inicia desde la raíz pasando ambos acumuladores en 0
#     return __contar(arbol.root, 0, 0)

# # Llamada directa que desempaqueta los dos valores devueltos
# cant_pares, cant_impares = contar_pares_impares(arbol)

# print(f"Cantidad de números pares: {cant_pares}")
# print(f"Cantidad de números impares: {cant_impares}")



# 2. Implementar una función que permita cargar una expresión matemática en un árbol binario(no balanceado), y resuelva lo siguiente:
# a. determinar cuál de los barridos muestra la expresión en el orden correcto;
# # b. resolver la expresión matemática y muestre el resultado.

arbol = BinaryTree()
cola = HeapMin()


def cargar_arbol_expresion(exp_matematica):
    # 1. Convertir la expresión infija (ej: "3+5*2") a postfija de forma simple
    salida = []
    pila_ops = []
    
    for c in exp_matematica:
        if c == " ":
            continue
        if c.isdigit():
            salida.append(c)
        else:
            # Si es operador, maneja la jerarquía básica (* / antes que + -)
            while pila_ops and pila_ops[-1] in "*/" and c in "+-":
                salida.append(pila_ops.pop())
            pila_ops.append(c)
            
    while pila_ops:
        salida.append(pila_ops.pop())

    # 2. Construir el árbol usando una pila de nodos
    pila_nodos = []
    
    for token in salida:
        # Creamos el nodo (reemplazá 'Node' por la clase de nodo que uses en tu TP)
        nodo = Node(token) 
        
        if token.isdigit():
            pila_nodos.append(nodo)
        else:
            # Si es operador, saca los dos últimos nodos para armar la sub-rama
            nodo.right = pila_nodos.pop()
            nodo.left = pila_nodos.pop()
            pila_nodos.append(nodo)
            
    # 3. Asignar la raíz del árbol
    arbol = BinaryTree()
    if pila_nodos:
        arbol.root = pila_nodos[0]
        
    return arbol

# --- EJECUCIÓN ---
exp_matematica = input("Ingrese una expresión matemática (ejemplo: 3+5*2): ")
arbol = cargar_arbol_expresion(exp_matematica)


print("\npreorden:")
arbol.preorden()

print("\ninorden:es el arbol en el orden correcto de la expresión matemática") 
arbol.inorden()

print("\npostorden:")
arbol.postorden()


# # b. resolver la expresión matemática y muestre el resultado.

def resolver_por_inorden(arbol: BinaryTree):
    expresion = []

    def __inorden(nodo):
        if nodo is not None:
            __inorden(nodo.left)
            expresion.append(str(nodo.value))
            __inorden(nodo.right)

    __inorden(arbol.root)
    
    # Separar los números y los operadores
    numeros = [x for x in expresion if x.isdigit()]
    operadores = [x for x in expresion if not x.isdigit()]

    # Alternar los elementos: Número -> Operador -> Número...
    cadena_partes = []
    for i in range(len(numeros)):
        cadena_partes.append(numeros[i])
        if i < len(operadores):
            cadena_partes.append(operadores[i])

    cadena = " ".join(cadena_partes)
    
    try:
        return eval(cadena)
    except SyntaxError:
        return "No se pudo evaluar la expresión"

# --- USO ---
resultado = resolver_por_inorden(arbol)
print(f"b. Resultado: {resultado}")



# 3. Desarrollar un algoritmo que permita cargar el índice del libro Ingeniería de Software de Ian Summerville de manera automática desde un archivo de texto, transformando el árbol n-ario
# del índice en un árbol binario no balanceado mediante el uso de la transformada de Knuth,para resolver las siguientes actividades:
# a. listar el índice en su orden original;
# b. mostrar la parte del índice correspondiente al subtitulo “Diseño de software
# de tiempo real”;
# c. deberá almacenar además del texto de índice la página del libro donde está dicho tema;
# d. determinar cuántos capítulos tiene;
# e. determinar todos los temas que contengan las palabras modelo y métrica.


indice_libro = [
    # (value, other_values -> (pagina, nivel))
    ("Capítulo 1: Introducción a la ingeniería de software", (1, 1)),
    ("1.1. Procesos de software", (15, 2)),
    ("1.1.1. Modelo en cascada", (18, 3)),
    ("1.1.2. Modelos evolutivos", (22, 3)),
    ("1.2. Métrica y calidad de software", (35, 2)),
    
    ("Capítulo 2: Gestión de proyectos", (45, 1)),
    ("2.1. Planificación de proyectos", (48, 2)),
    ("2.1.1. Estimación de costos", (52, 3)),
    
    ("Capítulo 11: Arquitecturas de sistemas", (250, 1)),
    ("11.1. Diseño de software de tiempo real", (275, 2)),
    ("11.1.1. Sistemas embebidos", (280, 3)),
    ("11.1.2. Modelo de sincronización y concurrencia", (290, 3)),
    ("11.1.3. Métrica de rendimiento en tiempo real", (295, 3)),
    ("11.2. Sistemas distribuidos", (310, 2))
]

def cargar_indice()