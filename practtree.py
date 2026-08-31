from tree import BinaryTree
from random import randint

# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria– que resuelva las siguientes actividades:
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

arbol = BinaryTree()

def cargar_arbol(arbol : BinaryTree):
    for i in range(10):
        arbol.insert_node(randint(0,20),None)


cargar_arbol(arbol)
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
print("arbol con barrido Preorden")
arbol.preorden()
print()
print("arbol con barrido Inorden")
arbol.inorden()
print()
print("arbol con barrido Postorden")
arbol.postorden()
print()
print("arbol con barrido Por Nivel")
print("falta implementar barrido por nivel")

print()
# b. determinar si un número está cargado en el árbol o no;

print("determinar si un número está cargado en el árbol o no")
print()
arbol.search(2)
aux = arbol.search(2)
if aux is not None:
    print(f"el valor {aux.value} se encuentra en el arbol")
else:
    print("el valor no se encuentra en el arbol")

print()

# c. eliminar tres valores del árbol;

print("eliminar tres valores del árbol")

print('eliminar', arbol.delete_node(20))
arbol.preorden()
print()
print('eliminar', arbol.delete_node(10))
arbol.preorden()
print()
print('eliminar', arbol.delete_node(5))
arbol.preorden()
print()
