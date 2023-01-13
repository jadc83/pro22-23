"""
70. Escribir la función numeros_pares que muestre por la consola los n primeros números
pares.
"""
from itertools import count
lista = []
def numeros_pares(numero):
    for x in range(2,numero + 1):
        print(x) if x % 2 == 0 else "hola"