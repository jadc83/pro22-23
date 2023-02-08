"""
19. Crear el archivo de texto «numeros_reales.txt» en el directorio de trabajo actual
que contenga una sola línea de texto con números reales separados por espacios. A
continuación, escribir un programa que abre ese archivo, lea los números que contiene
y calcule la suma y la media aritmética, mostrando los resultados por pantalla

"""
from functools import reduce

def suma(a, b):
    return a + b
    
fichero = open("numeros.txt", "r")
numeros = fichero.readline()
fichero.close()

numeros = numeros.split()
total = reduce(suma, [int(x) for x in numeros])
media = round(total / len(numeros),2)

print(f"La suma de los numeros contenidos en la linea es {total} y la media es {media} ")