"""
18. Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
luego las muestre en orden inverso a como se han introducido, desde la última cadena
introducida hasta la primera.
Indicación: Usar el método append sobre la lista y luego un bucle que recorra la lista
desde el último elemento hasta el primero.

"""

from functools import reduce
def suma(a, b):
    return a + b

i = 0
lista = []

while i != 10:
    lista.append(input("Mete cadena:\n"))
    i += 1

c = 0
lista1 = lista[::-1]

while c != 10:
    print(lista1[c])
    c += 1
