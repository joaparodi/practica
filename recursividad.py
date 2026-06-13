#1_Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.


# n = 4         4-(4-1)+3(3-1)+2(2-1)+1(1-0)     0=1

def fibbonacci_r(num : int) -> int:
    if num == 0 or num == 1:
        return num
    else:
        return fibbonacci_r(num -1) + fibbonacci_r(num - 2)
    
print(fibbonacci_r(7))



