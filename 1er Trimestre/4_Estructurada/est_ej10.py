"""
10. Escribir un programa que calcule el máximo común divisor de dos números enteros
introducidos por teclado, usando:
a) La función math.gcd.
b) Bucles.

"""

from math import gcd

num1 = int(input("Introduce primer numero: \n"))
num2 = int(input("Introduce segundo numero: \n"))

divisores = lambda n: tuple(filter(lambda d: n % d == 0,  range(1, n + 1 ) ) )

divs1 = divisores(num1)
divs2 = divisores(num2)

comunes = []
indice = 0
i = 0


