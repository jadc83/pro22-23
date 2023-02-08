"""
73. Escribir una función que decida si dos números enteros positivos son amigos. Dos
números a y b son amigos si la suma de los divisores propios (distintos de él mismo) de
a es igual a b, y viceversa.

Para probar, se pueden usar los números 220 y 284, que son amigos
"""

def divisores(numero):
    total = 0
    for x in range(1,numero):
        if numero % x == 0:
            total += x
    return total

def amigos(numero1, numero2):
    if divisores(numero1) == numero2 and divisores(numero2) == numero1:
        return "Son amiguis!"