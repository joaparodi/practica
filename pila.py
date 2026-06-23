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

# cargar(pila,datos_peliculas)
# pila.show()

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

# print("peliculas que marvel estudios estreno en 2016 :")
# peli_marvel(pila)


# 22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
# misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,costo de la recompensa. Resolver las siguientes actividades:
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.



class mision:
    def __init__(self,planeta,capturado,recompensa):
        self.planeta = planeta
        self.capturado = capturado
        self.recompensa = recompensa
    
    def __str__(self):
        return f"planeta:{self.planeta}--capturado:{self.capturado}--recompensa{self.recompensa}"
        
        
        
pila_boba = Stack()
pila_din = Stack()


# Datos para Boba Fett
datos_boba = [
    ("Tatooine", "Jabba the Hutt", 500),
    ("Bespin", "Han Solo", 5000),
    ("Nal Hutta", "Cad Bane", 2000)
]

# Datos para Din Djarin
datos_mando = [
    ("Nevarro", "Mythrol", 100),
    ("Arvala-7", "Grogu", 5000),
    ("Trask", "Mon Calamari", 300)
]

def carga_boba(pila_boba: Stack,datos_boba):
    for planeta,capturado,recompensa in datos_boba:
        x = mision(planeta,capturado,recompensa)
        pila_boba.push(x)

carga_boba(pila_boba,datos_boba)
print()
print("pila de boba fett")
print()
pila_boba.show()


def carga_din(pila_din : Stack , datos_mando):
    for planeta,capturado,recompensa in datos_mando:
        x = mision(planeta,capturado,recompensa)
        pila_din.push(x)

carga_din(pila_din,datos_mando)
print()
print("pila de Din Djarin:")
print()
pila_din.show()


# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;
print()
print("planetas visitados por boba fett:")
def visit_plan(pila: Stack):
    aux = Stack()
    while pila.size() > 0:
        aux.push(pila.pop())
    
    while aux.size() > 0:
        x = aux.pop()
        print(x.planeta)
        pila.push(x)

print()
visit_plan(pila_boba)
print()
print("planetas visitados por din:")
visit_plan(pila_din)
# pila_boba.show()


# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;

def rcaudado(pila):
    rec = 0
    aux = Stack()
    while pila.size() > 0 :
        aux.push(pila.pop())
        
    
    while aux.size() > 0 :
        x = aux.pop()
        rec += x.recompensa
        pila.push(x)
    return rec


print()
print("boba fett recaudo:")        
print(rcaudado(pila_boba))


print()
print("din recaudo :")
print(rcaudado(pila_din))
if rcaudado(pila_boba) > rcaudado(pila_din):
    print("Mayor fortuna: Boba Fett")
elif rcaudado(pila_din) > rcaudado(pila_boba):
    print("Mayor fortuna: Din Djarin")
else:
    print("Ambos recaudaron lo mismo.")


# c. determinar el número de la misión es decir su posición desde el fondo de la pila en la que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;

def cap_han(pila_boba):
    aux_boba = Stack()
    print("han solo fue capturado en la mision:")
    while pila_boba.size() > 0 :
        aux_boba.push(pila_boba.pop())
    
    for i in range(aux_boba.size()):
        x = aux_boba.pop()
        if x.capturado == "Han Solo":
            print(i+1)
        pila_boba.push(x)

print()        
cap_han(pila_boba)            

# pila_boba.show()


# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

def cant_capturas(pila):
    contador = 0
    aux = Stack()
    while pila.size()> 0 :
        aux.push(pila.pop())
        
    for i in range(aux.size()):
        x = aux.pop()
        if x.capturado != "":
            contador += 1
        pila.push(x)
    return contador


print()
cant_capturas(pila_boba)
print("la cantidad de capturas que realizo boba fett es de :")
print(cant_capturas(pila_boba))

print()

print("la cantidad de capturas que tuvo Din es de :")
print(cant_capturas(pila_din))


