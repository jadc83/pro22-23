"""
Escribir en Python una función completar() sin parámetros que lea un
archivo de texto llamado «datos.txt» con un texto similar a éste:

124*93*78
*********
*32*584*9

En cada línea del texto habrá una cadena de 9 caracteres formada por
dígitos y asteriscos, de forma que los dígitos no se pueden repetir
y puede haber muchos asteriscos (siempre que no se sobrepase la
longitud máxima de 9 caracteres en la línea).

La función deberá modificar el contenido del archivo, sustituyendo
los asteriscos por los dígitos que falten en esa línea, completando
de menor a mayor, de la siguiente forma:

124593678
123456789
132658479

De forma que:
- En la primera línea se han sustituido los asteriscos por 5 y 6
(en ese orden)
- En la segunda línea se han sustituido por todos los dígitos del
1 al 9 (en ese orden)
- En la tercera línea se han sustituido por 1, 6 y 7 (en ese orden).

Observación: Antes de cada test, se llama a completar() y luego se
almacena el contenido del archivo «datos.txt» en la lista lineas
(en cada elemento de la lista se guarda una línea del archivo),
eliminando los saltos de línea finales de cada línea.
"""

from functools import reduce
def suma(a, b):
        return a + b
final = []

def completar():
    fichero = open("prueba.txt", "r")
    while True:
        linea = fichero.readline()
        lineas = [ x for x in linea ]
        if linea == '':
            break
        noestan = sorted(set('123456789').difference(linea))
        for x in lineas:
            if x == "*":
                i = lineas.index("*")
                lineas[i] = noestan[0]
                del noestan[0]
        fused = reduce(suma, lineas)
        final.append(fused)
    fichero.close()

    fichero = open("prueba.txt", "w")
    for x in final:
        fichero.write(x.strip() + "\n")
    fichero.close()

