from stack import Stack
from random import randint

pila = Stack()

#1. Determinar el número de ocurrencias de un determinado elemento en una pila.
for i in range(10):
    pila.push(randint(0 , 20))
    
#pila.show()

#num = int(input("ocurrencia a contar:"))
#conta = 0

#while pila.size()> 0 :
#    x =  pila.pop()
#    if x == num :
#        conta  += 1

#print("la cantidad de ocurrencias encontradas son:")
#print(conta)
    
#6. Leer una palabra y visualizarla en forma inversa.

pila = Stack()

#palabra = input("palabra a invertir:")

#for letra in palabra:
#    pila.push(letra)

# pila.show()

def invertir(pila):
    aux = Stack()
    aux2 = Stack()
    while pila.size () > 0 :
        x = pila.pop()
        aux.push(x)
        aux2.push(x)
    
    while aux2.size() > 0 :
        pila.push(aux2.pop())
    return aux

invert  = invertir(pila)
# print("pila invertida:")
# invert.show()



# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que

# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.



pilas_v = Stack()
pilas_vii = Stack() 

# personajes_v = ["Luke Skywalker", "Darth Vader", "Han Solo", "Leia Organa", "Yoda"]
# for p in personajes_v:
#     pilas_v.push(p)

# print("personajes V de The empire strikes back")
# pilas_v.show()

# personajes_vii = ["Han Solo", "Leia Organa", "Rey", "Finn", "Luke Skywalker", "Kylo Ren"]
# for p in personajes_vii:
#     pilas_vii.push(p)

# print("personajes del episodio VII “The force awakens”.")
# pilas_vii.show()


def p_ambos_epi(pilas_v, pilas_vii):
    interseccion = Stack()
    aux = Stack()
    while pilas_v.size () > 0 :
        x = pilas_v.pop()
        encontrado = False
        while pilas_vii.size () > 0 :
            y = pilas_vii.pop()
            if y == x:
                encontrado = True
            aux.push(y)
        
        while aux.size () > 0 :
            pilas_vii.push(aux.pop())
        
        if encontrado:
            interseccion.push(x)
    return interseccion

# result = p_ambos_epi(pilas_v,pilas_vii)# cuando returno algun valor debo acordarme de porner una variable para guardar el resultado

# print("los personajes que aparece en ambos son:")
# result.show()


# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, desarrollar las funciones 
# necesarias para resolver las siguientes actividades:

# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

class pelicula:
    def __init__(self, titulo,estudio,anio):
        self.titulo = titulo
        self.estudio = estudio
        self.anio = anio
    
    def __str__(self):
        return f"{self.titulo}----{self.estudio}---{self.anio}"


pila = Stack()

datos_peliculas = [
    ("Guardians of the Galaxy", "Marvel Studios", "2014"),
    ("Captain America: Civil War", "Marvel Studios", "2016"),
    ("Black Panther", "Marvel Studios", "2018"),
    ("Interstellar", "Warner Bros", "2014"),
    ("Doctor Strange", "Marvel Studios", "2016"),
    ("Avengers: Infinity War", "Marvel Studios", "2018")
]

def cargar(pila: Stack , datos_peliculas):
    for titulo,estudio,anio in datos_peliculas:
        x = pelicula(titulo,estudio,anio)
        pila.push(x)

cargar(pila,datos_peliculas)
pila.show()

# a. mostrar los nombre películas estrenadas en el año 2014;

def estre_2014(pila , aniobuscado):
    aux =Stack()
    while pila.size () > 0 :
        x = pila.pop()
        if x.anio == aniobuscado:
            print(x.titulo)
        aux.push(x)
        
    while aux.size() > 0:
        pila.push(aux.pop())

# print("esto son los nombres de las peliculas estrenadas en el año 2014")        
# estre_2014(pila,"2014")
#pila.show()

# b. indicar cuántas películas se estrenaron en el año 2018;
def peli_2018(pila,year)-> int:
    aux = Stack()
    counter = 0

    while pila.size() > 0 :
        x = pila.pop()
        if x.anio == year:
            counter += 1
        aux.push(x)
        
    while aux.size() > 0:
        pila.push(aux.pop())
    return counter
     

# result = peli_2018(pila,"2018")  
# print(f"la cantidad de  peliculas que se estrenados en 2018 es: {result} peliculas")
# pila.show()

# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
def peli_marvel(pila: Stack):
    aux = Stack()
    while pila.size() > 0 :
        x = pila.pop()
        if x.estudio == "Marvel Studios" and x.anio == "2016":
            print(x.titulo)
        aux.push(x)
    while aux.size() > 0:
        pila.push(aux.pop())

print("peliculas que marvel estudios estreno en 2016 :")
peli_marvel(pila)
