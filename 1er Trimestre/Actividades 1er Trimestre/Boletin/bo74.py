"""
74. Crear una función que devuelva una lista de números aleatorios enteros. Los parámetros
de la función serán: la cantidad de números aleatorios que se mostrarán y los valores
mínimos y máximos que estos pueden tomar.

"""

import random

def aleatorios(c, a, b):
    lista = []
    for x in range(1, c + 1):
        lista.append(random.randint(a, b))
    print(lista)