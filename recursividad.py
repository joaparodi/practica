#1_Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.


# n = 4         4-(4-1)+3(3-1)+2(2-1)+1(1-0)     0=1


#num = int(input("dar el numero para realizar la sucesion de fibbonacci:"))


def fibbonacci_r(num : int) -> int:
    if num == 0 or num == 1:
        return num
    else:
        return fibbonacci_r(num -1) + fibbonacci_r(num - 2)

#print("el resultado es:")    
#print(fibbonacci_r(num))



#2. Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.
# 0 + 1 + 2 + 3 + 4 =10

#numm = int(input("dar un numero :"))

def suma_entero(numm : int) -> int:
    if numm == 0:
        return numm
    else:
        return numm + suma_entero(numm -1)

#suma_entero(numm)
#print(suma_entero(numm))

#3. Implementar una función para calcular el producto de dos números enteros dados.
# 2x3 = 2*2*2=6

n1 = int(input("introduce el primer indice:"))
n2 = int(input("introduce el numero por el cual va a multiplicar:"))

def produc(n1 : int , n2 : int)-> int:
    if n2 == 0:
        return 0
    else:
        return (n1 + produc(n1 , n2-1))# 2  2+2

produc(n1 , n2)
print(produc(n1 ,n2))


