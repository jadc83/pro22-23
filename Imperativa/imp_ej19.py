"""
19. Crear el archivo de texto «numeros_reales.txt» en el directorio de trabajo actual
que contenga una sola línea de texto con números reales separados por espacios. A
continuación, escribir un programa que abre ese archivo, lea los números que contiene
y calcule la suma y la media aritmética, mostrando los resultados por pantalla.

"""
from functools import reduce

fichero = open("numeros_reales.txt", "r")
copiafichero = fichero.readline()
fichero.close()
staging = tuple(map( int, copiafichero.split()))
ready = staging[:]
final = reduce(lambda a, b: a + b, ready)
print("La suma es: " + str(final))
print("La media es: " + str(final / len(ready)))


