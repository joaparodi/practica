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

palabra = input("palabra a invertir:")

for letra in palabra:
    pila.push(letra)

pila.show()

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
print("pila invertida:")
invert.show()



