"""
9. Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
luego las muestre en orden inverso a como se han introducido, desde la última cadena
introducida hasta la primera.
Indicación: Usar el método append sobre la lista y luego un bucle que recorra la lista
desde el último elemento hasta el primero.

"""
lista = []
contador = 1
rango = -1

while len(lista) < 10:

    lista.append(input("Introduce cadena " + str(contador)+":"))
    contador += 1

while rango >= -10:

    print(lista[rango])
    rango -= 1
