
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
# def by_name(item):
#     return item.name

# def by_year(item):
#     return item.year



# a. eliminar el nodo que contiene la información de Linterna Verde

# lista.add_criterion("name",by_name)
# delete_value = lista.delete_value("Green Lantern", 'name')

# print("eliminar el nodo que contiene la información de Linterna Verde")
# print(f"valor eliminado {delete_value}")
# print()


# b. mostrar el año de aparición de Wolverine;
# print(" mostrar el año de aparición de Wolverine")
# buscado = lista.search( "Wolverine",'name')
# if buscado is not None:
#     print(f'anio de aparicion de {lista[buscado].name} es {lista[buscado].year}')
# else:
#     print('no esta en la lista')

# print()


# c. cambiar la casa de thor a Marvel;
# print("cambiar la casa de thor a Marvel;")
# thor = lista.search( "Thor",'name')
# lista[thor].house = "Marvel"
# if thor is not None:
#     print(f"la nueva casa de thor es:{lista[thor].house}")
# else:
#     print("no se encontro thor")

# print()
# # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# print("mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra traje o armadura")
# lista.filter_contain_on_bio(['traje','armadura'])
# print()

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;

# print("nombre y casa de los superheroes cuya fecha de aparicion es anterior a 1963")
# for hero in lista:
#     if hero.year < 1963:
#         print(hero)

# print()

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# print("casa a la que pertenece la mujer maravilla y capitana marvel:")
# capMarvel = lista.search("Capitana Marvel",'name')
# if capMarvel is not None:
#     print(f"la casa de capitana Marvel es:{lista[capMarvel].house}")
# else:
#     print("no esta la capitana marvel")

# mujerMaravilla = lista.search("Mujer Maravilla",'name')
# if mujerMaravilla is not None:
#     print(f"la casa de la mujer maravilla es:{lista[mujerMaravilla].house}")
# else:
#     print("no esta la mujer maravilla")

# print()



# g. mostrar toda la información de Flash y Star-Lord;
# print("mostrar la informacion de flash y de star-lord:")
# flash = lista.search("The Flash","name")
# if flash is not None:
#     print(f"informacion de flash: {lista[flash].bio}")
# else:
#     print("flash no se encontro")

# star_lord = lista.search("Star-Lord",'name')
# if star_lord is not None:
#     print(f"la informacion de Star-lord :{lista[star_lord].bio}")
# else:
#     print("no se encuentra en la lista Star-lord ")

# print()

# h. listar los superhéroes que comienzan con la letra B, M y S;
# print("lista de superheroes que empiezan con B , M , S:")
# lista.filter_start_with(("B","M","S"))
# print()

# i. determinar cuántos superhéroes hay de cada casa de comic.
# print("cantidad de superheroes que ahi por casa de comic:")

# dc = lista.count_by_field('house','DC')
# print(f"cantidad de superheroes de la casa de comic de DC es de:{dc} ")

# Marvel = lista.count_by_field('house','Marvel')

# print(f"cantidad de superheroes de la casa de comic de Marvel es de :{Marvel}")

# print()

# 7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
#d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

# lista = List()
# list_1 = List()
# list_2 = List()

# def cargar(lista: List):
#     for i in range(10):
#         lista.append(randint(0,10))

# cargar(list_1)
# cargar(list_2)
# print("lista 1:")
# list_1.show()
# print()
# print("lista 2:")
# print()
# list_2.show()
# print()

# a. concatenar dos listas, una atrás de la otra;

# list_1.unir_L(list_2)
# list_1.show()

# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden

# list_1.unir_sin_r(list_2)
# list_1.show()

# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;

# total_rep = list_1.contar_interseccion(list_2)
# print(f"el total de valores repetidos es : {total_rep}")

#d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

#list_1.vaciar_mostrando()




#8. Utilizando una lista doblemente enlazada, cargar una palabra carácter a carácter, y determinar si la misma es un palíndromo, sin utilizar ninguna estructura auxiliar.

# palabra = input("dar la palabra: ")

# lista = List()

# def cargar(lista : List):
#     for caracter in palabra:
#         lista.append(caracter)

# cargar(lista)
# lista.show()

# def es_palindromo(lista: List) -> bool:
#     # Índice que empieza al principio (0)
#     inicio = 0
#     # Índice que empieza al final (len - 1)
#     fin = len(lista) - 1
    
#     # Mientras los índices no se crucen
#     while inicio < fin:
#         # Si los caracteres en los extremos no coinciden, no es palíndromo
#         if lista[inicio] != lista[fin]:
#             return False
        
#         # Movemos los índices hacia el centro
#         inicio += 1
#         fin -= 1
        
#     return True

# if es_palindromo(lista):
#     print("la palabra es un palindromo")
# else:
#     print("la palabra no es un palindromo")     



# 9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
# la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un algoritmo que permita realizar la siguientes actividades:
# a. mostrar los alumnos ordenados alfabéticamente por apellido;
# b. indicar los alumnos que no desaprobaron ningún parcial;
# c. determinar los alumnos que tienen promedio mayor a 8,89;
# d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
# e. mostrar el promedio de cada uno de los alumnos;
# f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
# g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
# h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
# i. mostrar todos los alumnos que rindieron en el año 2020;
# j. debe modificar el TDA para implementar lista de lista.




alumnos_data = [
    {"nombre": "Juan", "apellido": "Perez", "legajo": 101},
    {"nombre": "Maria", "apellido": "Lopez", "legajo": 102},
    {"nombre": "Carlos", "apellido": "Lozano", "legajo": 103},
    {"nombre": "Ana", "apellido": "Martinez", "legajo": 104},
    {"nombre": "Luis", "apellido": "Gomez", "legajo": 105}
]


notas_data = {
    101: [
        {"materia": "Algoritmos y estructuras de datos", "nota": 9, "fecha": "15/04/2026"},
        {"materia": "Base de datos", "nota": 9, "fecha": "20/05/2026"}
    ],
    102: [
        {"materia": "Algoritmos y estructuras de datos", "nota": 4, "fecha": "15/04/2026"},
        {"materia": "Base de datos", "nota": 3, "fecha": "20/05/2020"}
    ],
    103: [
        {"materia": "Algoritmos y estructuras de datos", "nota": 10, "fecha": "15/04/2026"},
        {"materia": "Base de datos", "nota": 8, "fecha": "20/05/2026"}
    ],
    104: [
        {"materia": "Algoritmos y estructuras de datos", "nota": 6, "fecha": "15/04/2026"},
        {"materia": "Base de datos", "nota": 9, "fecha": "20/05/2026"}
    ],
    105: [
        {"materia": "Algoritmos y estructuras de datos", "nota": 2, "fecha": "15/04/2026"},
        {"materia": "Base de datos", "nota": 3, "fecha": "20/05/2020"}
    ]
}

# lista_n = List()
# lista = List()

class Alumno:
    def __init__(self,nombre,apellido,legajo):
        self.name = nombre
        self.lastname = apellido
        self.legajo = legajo
        self.nota = list()
    
    def __str__(self):
        return f"nombre:{self.name}-------apellido:{self.lastname}---------legajo:{self.legajo}"




class Nota:
    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha     
    def __str__(self):
        return f"materia:{self.materia}-----nota:{self.nota}-------fecha:{self.fecha}"





# def cargar_Alum(lista: List,alumnos_data):
#     for a in alumnos_data:
#         nuevo_alumno = Alumno(a["nombre"], a["apellido"], a["legajo"])     
#         lista.append(nuevo_alumno)

# cargar_Alum(lista,alumnos_data)
# lista.show()




# def cargar_notas_en_alumnos(lista: List, notas_data):
#     for alumno in lista:
#         # Buscamos si el legajo del alumno tiene notas en el diccionario
#         if alumno.legajo in notas_data:
#             for n in notas_data[alumno.legajo]:
#                 nueva_nota = Nota(n["materia"], n["nota"], n["fecha"])
#                 # Aquí está la clave: guardamos la nota en la sub-lista del alumno
#                 alumno.nota.append(nueva_nota)

# cargar_notas_en_alumnos(lista,notas_data)
# lista.show()


# a. mostrar los alumnos ordenados alfabéticamente por apellido;
# def by_lastname(item):
#     return item.lastname

# lista.add_criterion('lastname',by_lastname)

# lista.sort_by_criterion("lastname")
# print()
# lista.show()

# print()
# b. indicar los alumnos que no desaprobaron ningún parcial;

# def mostrar_alumnos_sin_desaprobados(lista):
#     print("Alumnos que aprobaron todos los parciales:")
    
#     for alumno in lista:
#         # Supongamos que 4 es la nota mínima para aprobar
#         tiene_desaprobados = False
        
#         # Recorremos la sub-lista de notas del alumno
#         for nota in alumno.nota:
#             if nota.nota < 4:
#                 tiene_desaprobados = True
#                 break # Si tiene un desaprobado, dejamos de revisar a este alumno
        
#         # Si la bandera sigue siendo False, el alumno no desaprobó nada
#         if not tiene_desaprobados:
#             print(f"- {alumno.lastname}, {alumno.name}")

# mostrar_alumnos_sin_desaprobados(lista)


# c. determinar los alumnos que tienen promedio mayor a 8,89;
# print()

# def mostrar_promedios_altos(lista):
#     print("--- Alumnos con promedio mayor a 8.89 ---")
    
#     # Recorremos la lista principal de alumnos
#     for alumno in lista:
#         # Reiniciamos variables por cada alumno
#         total = 0
#         contador = 0
        
#         # Recorremos la sub-lista de notas de ESTE alumno
#         for nota_obj in alumno.nota:
#             total += nota_obj.nota
#             contador += 1
        
#         # Calculamos el promedio si el alumno tiene al menos una nota
#         if contador > 0:
#             promedio = total / contador
#             if promedio > 8.89:
#                 print(f"{alumno.lastname}, {alumno.name} - Promedio: {promedio:.2f}")

# Llamada a la función
# mostrar_promedios_altos(lista)
# print()

# d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
# print("la información de los alumnos cuyos apellidos comienzan con L:")
# lista.filter_start_with_ape(("L"))

print()
# e. mostrar el promedio de cada uno de los alumnos;
# print("promedio de cada alumno")

# def mostrar_promedios(lista):
#     for alumno in lista:
#         total = 0
#         contador = 0
#         for nota_obj in alumno.nota:
#             total += nota_obj.nota
#             contador += 1
#         if contador > 0:
#             promedio = total / contador
#             print(f"{alumno.lastname}, {alumno.name} - Promedio: {promedio:.2f}")
#         else:
#             print(f"{alumno.lastname}, {alumno.name} - Sin notas")



# mostrar_promedios(lista)
# print()

# f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
# print("alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”:")
# def rindieron_alg(lista):
#     for alumno in lista:
#         for nota_obj in alumno.nota:
#             x = nota_obj
#             if x.materia ==  "Algoritmos y estructuras de datos":
#                 print(f"{alumno.lastname}, {alumno.name}")
#                 # Encontramos la materia, podemos pasar al siguiente alumno
#                 break

# rindieron_alg(lista)


# g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
# print()
# print("indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario")

# buscado = input("ingrese el nombre del alumno a buscar:")

# def alumno_buscado(lista,buscado):
#     encontrado = False
#     for alumno in lista:
#         if alumno.name == buscado:
#             encontrado = True
#             total_notas = len(alumno.nota)
#             if total_notas == 0:
#                 print("El alumno no tiene notas cargadas.")
#                 return

#             # Contamos cuántas materias aprobó (nota >= 4)
#             aprobadas = 0
#             for nota_obj in alumno.nota:
#                 if nota_obj.nota >= 4:
#                     aprobadas += 1
            
#             # Calculamos el porcentaje
#             porcentaje = (aprobadas / total_notas) * 100
#             print(f"El porcentaje de aprobados de {alumno.name} {alumno.lastname} es: {porcentaje:.2f}%")
#             break
#     if not encontrado:
#         print("Error: El alumno no se encuentra en la lista.")
        
        
# alumno_buscado(lista,buscado) 
# print()

# h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
# print("indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”")
# lista_a = List()
# lista_d = List()
# def apro_des_base(lista,lista_a,lista_d):
#     apro = 0
#     des = 0
#     for alumno in lista:
#         for nota_obj in alumno.nota:
#             if nota_obj.materia == "Base de datos":
#                 if nota_obj.nota > 4 :
#                     lista_a.append(alumno)
#                     apro += 1
#                 else:
#                     lista_d.append(alumno)
#                     des += 1
#     return apro,des

# aprobados,desaprobados = apro_des_base(lista,lista_a,lista_d)

# print()
# print(f"aprobados:{aprobados}")
# lista_a.show()
# print()
# print(f"desaprobados:{desaprobados}")
# lista_d.show()


# i. mostrar todos los alumnos que rindieron en el año 2020;
# lista_rin_2020 = List()

# def alum_2020(lista,lista_rin_2020):
#     for alumno in lista:
#         for nota_obj in alumno.nota:
#             if "2020" in nota_obj.fecha :#compara en la cadena si esta ese valor
                
#                 lista_rin_2020.append(alumno)
#                 break
            
            
# alum_2020(lista,lista_rin_2020)
# print()
# print("lista de los alumnos que rindieron en el 2020:")
# lista_rin_2020.show()


# j. debe modificar el TDA para implementar lista de lista.
#ya lo hice al crear la clase de alumnos y adentro ponerle lo de self.nota = List()




# 10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista, duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que
# permita realizar las siguientes actividades:
# a. obtener la información de la canción más larga;
# b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
# c. obtener todas las canciones de la banda Arctic Monkeys;
# d. mostrar los nombres de las bandas o artistas que solo son de una palabra.

class Canciones:
    def __init__(self,nombre,artistas,duracion,cant_repro):
        self.name = nombre
        self.artist = artistas
        self.time = duracion
        self.cant = cant_repro
    
    def __str__(self):
        return f"nombre:{self.name}------artistas o banda:{self.artist}------duracion:{self.time}-------reproduciones:{self.cant}"



# Lista de diccionarios con la información de las canciones
spotify_data = [
    {"nombre": "Do I Wanna Know?", "artista": "Arctic Monkeys", "duracion": 272, "reproducciones": 1500000},
    {"nombre": "Bohemian Rhapsody", "artista": "Queen", "duracion": 354, "reproducciones": 2000000},
    {"nombre": "Yellow", "artista": "Coldplay", "duracion": 269, "reproducciones": 1200000},
    {"nombre": "R U Mine?", "artista": "Arctic Monkeys", "duracion": 201, "reproducciones": 900000},
    {"nombre": "Blinding Lights", "artista": "The Weeknd", "duracion": 200, "reproducciones": 3000000},
    {"nombre": "Starlight", "artista": "Muse", "duracion": 240, "reproducciones": 800000},
    {"nombre": "Human", "artista": "Rag'n'Bone Man", "duracion": 199, "reproducciones": 1100000},
    {"nombre": "Levitating", "artista": "Dua Lipa", "duracion": 203, "reproducciones": 2500000},
    {"nombre": "Imagine", "artista": "John Lennon", "duracion": 183, "reproducciones": 1800000},
    {"nombre": "Thriller", "artista": "Michael Jackson", "duracion": 357, "reproducciones": 2200000}
]

lista = List()

def cargar(lista:List,spotify_data):#se pone en la clase cancion los nombres entre comillas que tiene el diccionario
    for cancion in spotify_data:
        lista.append(Canciones(cancion["nombre"],cancion["artista"],cancion["duracion"],cancion["reproducciones"]))

cargar(lista,spotify_data)
lista.show()
print()

# a. obtener la información de la canción más larga;
def cancion_mas_larga(lista):
    lista_l = None
    maximo = 0
    for cancion in lista:
        if cancion.time > maximo:
            maximo = cancion.time
            lista_l =cancion
    return lista_l
   

lista_m_larga = cancion_mas_larga(lista)
if lista_m_larga:
    print(lista_m_larga)
else:
    print("no existe ninguna cancion")


# b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
def mostrar_top(lista, n):
    lista.sort_by_criterion('repro') 
    
    print(f"\n--- TOP {n} canciones ---")
    contador = 0
    for cancion in lista:
        if contador < n:
            print(f"{contador + 1}: {cancion.name} ({cancion.cant} repros)")
            contador += 1
        else:
            break # Cuando llegamos al límite, cortamos el bucle

# Uso:
mostrar_top(lista, 5)
mostrar_top(lista, 10)
mostrar_top(lista, 40)

# c. obtener todas las canciones de la banda Arctic Monkeys;
def can_ban(lista):
    lista_b = None
    for cancion in lista:
        if cancion.name == "Arctic Monkeys":
            x = cancion.






