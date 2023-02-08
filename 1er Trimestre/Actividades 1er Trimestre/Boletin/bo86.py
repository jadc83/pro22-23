"""
86. Leer y almacenar n números enteros en una lista, a partir de la que se construirán otras
dos listas con los elementos con valores pares e impares de la primera, respectivamente.
Las listas con valores pares e impares deberán mostrarse ordenadas.

"""
import random
cantidad = int(input("Cuantos numeros quiere almacenar:\n"))
numeros = [ random.randint(1,1000) for x in range(1,cantidad + 1)]
lista1 = []
lista2 = []
for x in numeros:
    if x % 2 == 0:
        lista1.append(x)
    else:
        lista2.append(x)
        
lista1 = sorted(lista1)
lista2 = sorted(lista2)

print(f"Pares: {lista1}\n Impares: {lista2}")