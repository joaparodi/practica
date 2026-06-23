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

# n1 = int(input("introduce el primer indice:"))
# n2 = int(input("introduce el numero por el cual va a multiplicar:"))

def produc(n1 : int , n2 : int)-> int:
    if n2 == 0:
        return 0
    else:
        return (n1 + produc(n1 , n2-1))# 2  2+2
#


#4. Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.

#2^2 = 2x2   2^3 = (2x2)x2

# num1 = int(input("dar el valor del exponente:"))
# num2 = int(input("ingrese la potencia del exponente:"))

def potencia(num1 : int,num2 : int)-> int:
    if num2 == 1:
        return num1
    else:
        return num1 * potencia(num1 , num2-1)

# potencia(num1,num2)
# print(potencia(num1,num2))


#5. Desarrollar una función que permita convertir un número romano en un número decimal.

# romano = input("ingrese el numero romaro :")

def tranf_romano(romano):
    valores = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    i = 0
    def convertir(i) :
        if i >= len(romano):
            return 0
        if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i + 1]]:
            return valores[romano[i + 1]] - valores[romano[i]] + convertir(i + 2)
        else:
            return valores[romano[i]] + convertir(i + 1)
    return convertir(0)

# tranf_romano(romano)
# print(tranf_romano(romano))



#7. Desarrollar un algoritmo que permita calcular la siguiente serie:
#1/n-1 + 1/n-1

n = int(input("ingrese un numero:"))

def serie_n(n):
    if n == 1:
        return 1
    else:
        return 1/n + serie_n(n-1)

serie_n(n)
print(serie_n(n))

