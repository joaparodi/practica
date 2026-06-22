from queue import Queue
from random import randint





#1. Eliminar de una cola de caracteres todas las vocales que aparecen.

# cola = Queue()


# vocales =['a','e','i','o','u']

# for i in range(10):
#     cola.arrive(chr(randint(97,122)))

# print("cola con vocales:")
# cola.show()

# def eleminar_v(cola : Queue,vocales : tuple):
#     colaaux = Queue()
#     while cola.size() > 0 :
#         x = cola.attention()
#         if x not in vocales:
#             colaaux.arrive(x)
       
#     while colaaux.size() > 0:
#         cola.arrive(colaaux.attention())


# print("cola sin vocales:")    
# eleminar_v(cola,vocales)
# cola.show()



#4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

cola = Queue()

def cargar(cola):
    for i in range(10):
        cola.arrive(randint(0,20))

cargar(cola)

# print("cola con numeros:")
# cola.show()

def es_primo(n):
    if n <= 1: 
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: 
                return False
        return True


def no_es_primo(cola):
    colaaux = Queue()
    for i in range(cola.size()):
        x = cola.attention()
        if es_primo(x):
            colaaux.arrive(x)
     
    
    while colaaux.size() > 0 :
        cola.arrive(colaaux.attention())

# no_es_primo(cola)
# print("cola sin numeros primos")
# cola.show()



#6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.

cola = Queue()

def cargar(cola):
    for i in range(10):
        cola.arrive(randint(0,20))

cargar(cola)
cola.show()

elemento = int(input("dame la ocurrencia a contar:"))

def cant_ocurrencia(cola,elemento):
    cant = 0
    for i in range(cola.size()):
        x = cola.on_front()
        if x == elemento:
            cant += 1
        cola.move_to_end()
    return cant


result = cant_ocurrencia(cola,elemento)
print(f"cantidad de veces que se repite la ocurrencia:{result}")
cola.show()





