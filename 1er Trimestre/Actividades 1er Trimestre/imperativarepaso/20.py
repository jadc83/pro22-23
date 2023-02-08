"""
20. Crear un archivo de texto con una colección de números reales, uno por línea. A
continuación, escribir un programa que:
a. Abra el archivo para lectura.
b. Lea todas sus líneas.
c. Muestre finalmente la suma de todos ellos.

"""
from functools import reduce

def suma(a, b):
    return a + b

numeros = []
fichero = open("numeros2.txt", "r")
numeros += [int(x) for x in fichero.readlines()]
res = reduce(suma, numeros)
print(res)

