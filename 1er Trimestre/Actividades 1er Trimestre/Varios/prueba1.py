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
def completar():
    todos = [ "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    final = []

    def suma(num1, num2):
        return num1 + num2

    def no_estan(cadena):
        diferentes = sorted(lista.difference(cadena))
        return diferentes

    with open("datos.txt", "r", encoding='UTF-8') as fichero:
        while True:
            linea = fichero.readline()
            if linea == '':
                break

            lista = set(todos)
            lista2 = set([x for x in linea])
            noestan = no_estan(lista2)
            lista2 = list(linea)

            for x in lista2:
                if x == "*":
                    lista2[lista2.index("*")] = noestan[0]
                    del noestan[0]

            lista3 = reduce(suma, lista2)
            final.append(lista3)
    with open("datos.txt", "w", encoding='UTF-8') as fichero:
        fichero.writelines(final)

hola = [1,3,5,7,9]
adios = {1,2,4,6,8,10}

res = adios.difference(hola)

