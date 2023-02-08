"""
17. Escribir un programa que calcule la media de cinco valores numéricos reales (tipo float)
introducidos por teclado.

"""
from functools import reduce

def suma(a, b):
    return a + b

i = 0

lista = []

while i != 5:
    lista.append(float(input("Mete numero:\n")))
    i += 1

media = reduce(suma, lista) / len(lista)

print(f"La media de {tuple(x for x in lista)} es {media}")