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
    x =  pila.pop()
    if x == num :
        conta  += 1

#print("la cantidad de ocurrencias encontradas son:")
#print(conta)
    
