"""
4. 
Escribir un programa que:
    1:lea los coeficientes a2 , a1 y a0 de un polinomio de segundo grado Y escriba ese polinomio.

                        (a2 * x**2) + (a1 * x) + a0

    2: lea el valor de x y escriba qué valor toma el polinomio para esa x.

Para facilitar la salida, se supondrá que los coeficientes y x son enteros.
Por ejemplo, si los coeficientes y x son 1, 2, 3 y 2, respectivamente, la salida puede ser:

1x^2 + 2x + 3

a * x**2 + (b * x) + c

(1 * x**2) + (2 * x) + 3

a * x**2 + 2x + c
a        +  b + c

"""

a = 1
b = 2
c = 6

from math import sqrt

def p(n):
    def p1(a,b,c):
        nonlocal n
        return a * n**2 + b * n + c
    return p1(a,b,c)


"""

try:
    disc = sqrt(pow( b, 2 ) - 4 * a * c )
    arriba1 = (-b - disc ) / (2 * a) 
    arriba2 = (-b + disc ) / (2 * a)
    print(arriba1, arriba2)
except ValueError:
    print("Error, El discriminante no es positivo.")

"""