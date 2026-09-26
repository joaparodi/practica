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
cola = Queue()


exp_matematica = input("Ingrese una expresión matemática (ejemplo: 3+5*2): ")

def cargar_expresion(arbol: BinaryTree, cola: Queue, exp_matematica: str):
    # 2. Convertir y encolar
    for i in range(len(exp_matematica)):
        caracter = exp_matematica[i]
        if caracter != " ":
            # Si es un número lo convierte a entero, si es un operador lo deja como string
            if caracter.isdigit():
                cola.arrive(int(caracter))
            else:
                cola.arrive(caracter)
            
    # 3. Desencolar e insertar en el árbol
    while cola.size() > 0:
        arbol.insert_node_expresion(cola.attention(), None)

# --- EJECUCIÓN Y BARRIDOS ---
cargar_expresion(arbol, cola, exp_matematica)

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

