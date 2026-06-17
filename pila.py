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


pila = Stack()
pilas_v = Stack()
pilas_vii = Stack() 

personajes_v = ["Luke Skywalker", "Darth Vader", "Han Solo", "Leia Organa", "Yoda"]
for p in personajes_v:
    pilas_v.push(p)

print("personajes V de The empire strikes back")
pilas_v.show()

personajes_vii = ["Han Solo", "Leia Organa", "Rey", "Finn", "Luke Skywalker", "Kylo Ren"]
for p in personajes_vii:
    pilas_vii.push(p)

print("personajes del episodio VII “The force awakens”.")
pilas_vii.show()


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

result = p_ambos_epi(pilas_v,pilas_vii)# cuando returno algun valor debo acordarme de porner una variable para guardar el resultado

print("los personajes que aparece en ambos son:")
result.show()