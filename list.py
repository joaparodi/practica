from list_ import List


# 1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

# Así representamos los nodos de forma simple (usando una lista común)
# [dato, siguiente_nodo]
n3 = ["Leia", None]
n2 = ["Yoda", n3]
n1 = ["Luke", n2]

# La lista es simplemente el primer nodo
cabeza = n1

# Para contar, solo recorres la cadena
def contar(nodo):
    total = 0
    while nodo is not None:
        total += 1
        nodo = nodo[1]  # Saltas al siguiente (que está en la posición 1)
    return total

print("Cantidad de nodos:", contar(cabeza))




