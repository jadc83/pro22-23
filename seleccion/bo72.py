"""
72. Escribir la función divisores_primos que devuelva una lista con todos los divisores
primos del número entero que se le pasa como argumento.
"""
from itertools import count

            
lista = []

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def divisores(numero):
    for x in range(2,numero):
        if numero % x == 0:
            if es_primo(x):
                print(x)