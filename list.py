
from random import randint
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

# print("Cantidad de nodos:", contar(cabeza))




#3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,una que contenga los números pares y otra para los números impares.

lista_par = List()
lista_impar = List()

lista = List()

def cargar(lista):
    for i in range(10):
        lista.append(randint(0,20))

cargar(lista)
print("lista")
lista.show()
print()

def separador_par(lista,lista_par,lista_impar):
    aux = List()
    for i in range(lista.size()):
        x = lista[i]
        if x % 2 == 0:
            lista_par.append(x)
        else:
            lista_impar.append(x)
        aux.append(x)
    
   
        
        
separador_par(lista,lista_par,lista_impar)  
print("lista con numero impar:")
print()
lista_impar.show()
print()
print("lista con numeros par:")
lista_par.show()
print()
lista.show()
print()


#5. Dada una lista de números enteros eliminar de estas los números primos.

# lista = List()

# def cargar(lista: List):
#     for i in range(10):
#         lista.append(randint(0,20))

# cargar(lista)
# lista.show()












