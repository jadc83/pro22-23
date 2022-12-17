"""
10. Escribir un programa que calcule el máximo común divisor de dos números enteros
introducidos por teclado, usando:
a) La función math.gcd.
b) Bucles.


el máximo común divisor de dos números se puede encontrar dividiendo 
el número mayor por el número menor. Si la división es exacta, el m.c.d.
es el número menor. Si la división no es exacta, entonces se toma el residuo,
y se divide tantas veces como haga falta para llegar a una división sin residuo. 

El m.c.d. es el último número por cuál se puede dividir. 
"""

#num1 = int(input("Introduce primer numero:\n"))
#num2 = int(input("Introduce segundo numero:\n"))
#menor = num1 if num1 <= num2 else num2
#mayor = num1 if num1 >= num2 else num2

def mcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b