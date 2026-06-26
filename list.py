
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
# print("lista")
# lista.show()
# print()

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
# print("lista con numero impar:")
# print()
# lista_impar.show()
# print()
# print("lista con numeros par:")
# lista_par.show()
# print()
# lista.show()
# print()


#5. Dada una lista de números enteros eliminar de estas los números primos.

lista = List()

def cargar(lista: List):
    for i in range(10):
        lista.append(randint(0,20))

cargar(lista)
# lista.show()

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def elimi_primo(lista: List):
    temp = List()
    for i in range(lista.size()):
        x = lista[i]
        if not es_primo(x):
            temp.append(x)
    
    while lista.size() > 0 :
        lista.remove(lista[0])
    
    for elemento in temp:
        lista.append(elemento)    
    
            
elimi_primo(lista)
# print()
# print("lista sin los numeros primos :")
# lista.show()



# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.



superheroes = [
    {
      "nombre": "Spider-Man",
      "anio_aparicion": 1962,
      "casa": "Marvel",
      "biografia": "Peter Parker fue mordido por una araña radiactiva y obtuvo poderes de superhéroe. Trabaja como fotógrafo freelance en el Daily Bugle mientras protege Nueva York."
    },
    {
      "nombre": "Iron Man",
      "anio_aparicion": 1963,
      "casa": "Marvel",
      "biografia": "Tony Stark, genio multimillonario e inventor, construyó una armadura tecnológica para escapar de sus captores. Fundador de los Vengadores y director de Stark Industries."
    },
    {
      "nombre": "Wolverine",
      "anio_aparicion": 1974,
      "casa": "Marvel",
      "biografia": "Logan posee un esqueleto recubierto de adamantium y garras retráctiles. Su factor de curación acelerada lo hace casi inmortal. Miembro icónico de los X-Men."
    },
    {
      "nombre": "Thor",
      "anio_aparicion": 1962,
      "casa": "DC",
      "biografia": "Dios nórdico del trueno e hijo de Odín. Empuña el martillo Mjolnir y defiende tanto Asgard como la Tierra. Miembro fundador de los Vengadores."
    },
    {
      "nombre": "Black Widow",
      "anio_aparicion": 1964,
      "casa": "Marvel",
      "biografia": "Natasha Romanoff fue entrenada desde niña en el programa Habitación Roja. Es una espía y agente de élite de S.H.I.E.L.D., experta en artes marciales y tecnología."
    },
    {
      "nombre": "Batman",
      "anio_aparicion": 1939,
      "casa": "DC",
      "biografia": "Bruce Wayne presenció el asesinato de sus padres de niño y juró proteger Gotham. Sin poderes, usa su inteligencia, fortuna y entrenamiento físico para combatir el crimen. Usando un traje con muchas herramientas"
    },
    {
      "nombre": "Superman",
      "anio_aparicion": 1938,
      "casa": "DC",
      "biografia": "Kal-El fue enviado desde el planeta Krypton antes de su destrucción. Adoptado como Clark Kent en Kansas, usa sus poderes solares para defender la Tierra."
    },
    {
      "nombre": "Mujer Maravilla",
      "anio_aparicion": 1941,
      "casa": "DC",
      "biografia": "Diana, princesa de las Amazonas de la isla Temyscira, fue criada como guerrera. Porta el lazo de la verdad y las brazaletes indestructibles. Embajadora de paz y justicia."
    },
    {
      "nombre": "The Flash",
      "anio_aparicion": 1956,
      "casa": "DC",
      "biografia": "Barry Allen era un científico forense que fue alcanzado por un rayo durante un experimento. Obtuvo la capacidad de moverse a velocidades superlumínicas conectado a la Fuerza de la Velocidad."
    },
    {
      "nombre": "Green Lantern",
      "anio_aparicion": 1959,
      "casa": "DC",
      "biografia": "Hal Jordan fue elegido por el anillo de poder de los Guardianes del Universo. El anillo le permite crear construcciones de energía verde limitadas solo por su voluntad e imaginación."
    }
]



lista = List()


class Superheroes:
    def __init__(self,nombre,anio_ap,casa,bio):
        self.name = nombre
        self.year = anio_ap
        self.house = casa
        self.bio = bio
        
    def __str__(self):
        return f"nombre:{self.name}------año de aparicion:{self.year}---------casa:{self.house}--------biografia:{self.bio}"
        

def cargar(lista,superheroes):
    for hero in superheroes:
        lista.append(Superheroes(hero["nombre"],hero["anio_aparicion"],hero["casa"],hero["biografia"]))



cargar(lista,superheroes)
# lista.show()

#criterios
def by_name(item):
    return item.name

def by_year(item):
    return item.year



# a. eliminar el nodo que contiene la información de Linterna Verde

lista.add_criterion("name",by_name)
delete_value = lista.delete_value("Green Lantern", 'name')

print("eliminar el nodo que contiene la información de Linterna Verde")
print(f"valor eliminado {delete_value}")
print()


# b. mostrar el año de aparición de Wolverine;
print(" mostrar el año de aparición de Wolverine")
buscado = lista.search( "Wolverine",'name')
if buscado is not None:
    print(f'anio de aparicion de {lista[buscado].name} es {lista[buscado].year}')
else:
    print('no esta en la lista')

print()


# c. cambiar la casa de thor a Marvel;
print("cambiar la casa de thor a Marvel;")
thor = lista.search( "Thor",'name')
lista[thor].house = "Marvel"
if thor is not None:
    print(f"la nueva casa de thor es:{lista[thor].house}")
else:
    print("no se encontro thor")

print()
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print("mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra traje o armadura")
lista.filter_contain_on_bio(['traje','armadura'])
print()

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;

print("nombre y casa de los superheroes cuya fecha de aparicion es anterior a 1963")
for hero in lista:
    if hero.year < 1963:
        print(hero)

print()

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print("casa a la que pertenece la mujer maravilla y capitana marvel:")
capMarvel = lista.search("Capitana Marvel",'name')
if capMarvel is not None:
    print(f"la casa de capitana Marvel es:{lista[capMarvel].house}")
else:
    print("no esta la capitana marvel")

mujerMaravilla = lista.search("Mujer Maravilla",'name')
if mujerMaravilla is not None:
    print(f"la casa de la mujer maravilla es:{lista[mujerMaravilla].house}")
else:
    print("no esta la mujer maravilla")

print()



# g. mostrar toda la información de Flash y Star-Lord;
print("mostrar la informacion de flash y de star-lord:")
flash = lista.search("The Flash","name")
if flash is not None:
    print(f"informacion de flash: {lista[flash].bio}")
else:
    print("flash no se encontro")

star_lord = lista.search("Star-Lord",'name')
if star_lord is not None:
    print(f"la informacion de Star-lord :{lista[star_lord].bio}")
else:
    print("no se encuentra en la lista Star-lord ")

print()

# h. listar los superhéroes que comienzan con la letra B, M y S;
print("lista de superheroes que empiezan con B , M , S:")
lista.filter_start_with(("B","M","S"))
print()

# i. determinar cuántos superhéroes hay de cada casa de comic.
print("cantidad de superheroes que ahi por casa de comic:")

dc = lista.count_by_house('DC')
print(f"cantidad de superheroes de la casa de comic de DC es de:{dc} ")

Marvel = lista.count_by_house('Marvel')

print(f"cantidad de superheroes de la casa de comic de Marvel es de :{Marvel}")



