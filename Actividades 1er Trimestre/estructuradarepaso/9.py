"""
9. Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
luego las muestre en orden inverso a como se han introducido, desde la última cadena
introducida hasta la primera.
Indicación: Usar el método append sobre la lista y luego un bucle que recorra la lista
desde el último elemento hasta el primero.

"""

lista = []

while len(lista) != 5:
    lista.append(input("Mete cadena aqui:\n"))

while len(lista) != 0:
    print(lista[-1])
    del lista[-1]