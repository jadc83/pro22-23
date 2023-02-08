"""
43. Diseñar un programa que muestre la suma de los 10 primeros números impares
"""
from itertools import count
contador = 0
lista = []
while contador < 10:
    for x in count():
        if x % 2 != 0:
            lista.append(x)
            contador += 1
            if contador > 10:
                break
total = sum(lista)
print(total)
        