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

# cargar(cola)
# cola.show()

# elemento = int(input("dame la ocurrencia a contar:"))

def cant_ocurrencia(cola,elemento):
    cant = 0
    for i in range(cola.size()):
        x = cola.on_front()
        if x == elemento:
            cant += 1
        cola.move_to_end()
    return cant


# result = cant_ocurrencia(cola,elemento)
# print(f"cantidad de veces que se repite la ocurrencia:{result}")
# cola.show()



# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks



class per_star_wars:
    def __init__(self,nombre,planeta):
        self.nombre = nombre
        self.planeta = planeta
    
    def __str__(self):
        return f"nombre:{self.nombre}----planeta:{self.planeta}"


personajes_star_wars = [
    {"nombre": "Luke Skywalker", "planeta": "Tatooine"},
    {"nombre": "Leia Organa", "planeta": "Alderaan"},
    {"nombre": "Han Solo", "planeta": "Corellia"},
    {"nombre": "Yoda", "planeta": "Dagobah"},
    {"nombre": "Jar Jar Binks", "planeta": "Naboo"},
    {"nombre": "Ewoks", "planeta": "Endor"},
    {"nombre": "Darth Vader", "planeta": "Tatooine"}
]

cola = Queue()

def cargar(cola,personajes_star_wars):
    for p in personajes_star_wars:
        cola.arrive(per_star_wars(p["nombre"],p["planeta"]))

cargar(cola,personajes_star_wars)
cola.show()
print()

# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
def plant_alde_endor_tatooi(cola: Queue):
    colaux = Queue()
    for i in range(cola.size()):
        x = cola.on_front()
        if x.planeta == "Alderaan" or x.planeta == "Endor" or x.planeta == "Tatooine":
            colaux.arrive(x)
        cola.move_to_end()
    colaux.show()
print("personajes del planeta Alderaan, Endor y Tatooine: ")
plant_alde_endor_tatooi(cola)
print()


# c. insertar un nuevo personaje antes del maestro Yoda
new= input("ingresa el personaje que va ates del maestro yoda:")
plan = input("ingresa el planeta:")

def ant_yoda(cola,new,plan):
    encontrado = False
    aux =Queue()
    while cola.size() > 0:
        x = cola.attention()
        if x.nombre == "Yoda":
            aux.arrive(per_star_wars(new,plan))
            encontrado = True
        aux.arrive(x)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    return encontrado


if not ant_yoda(cola, new, plan):
    print("El maestro Yoda no está en la cola.")
else:
    print("Personaje insertado con éxito.")

cola.show()
        