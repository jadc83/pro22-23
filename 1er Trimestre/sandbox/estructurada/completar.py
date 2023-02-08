"""
Escribir en Python una función completar() sin parámetros que lea un archivo de texto llamado «datos.txt» con un texto similar a éste:

124*93*78
*********
*32*584*9

En cada línea del texto habrá una cadena de 9 caracteres formada por dígitos y asteriscos, de forma que los 
dígitos no se pueden repetir y puede haber muchos asteriscos (siempre que no se sobrepase la longitud máxima 
de 9 caracteres en la línea).

La función deberá crear un archivo nuevo llamado «resultados.txt» que contenga el mismo contenido que el archivo 
«datos.txt» original, pero sustituyendo los asteriscos por los dígitos que falten en esa línea, completando de 
menor a mayor, de la siguiente forma:

124593678
123456789
132658479

De forma que:
en la primera línea se han sustituido los asteriscos por 5 y 6 (en ese orden),
en la segunda línea se han sustituido por todos los dígitos del 1 al 9 (en ese orden), y
en la tercera línea se han sustituido por 1, 6 y 7 (en ese orden).

Observación: Antes de cada test, se llama a completar() y luego se almacena el contenido del archivo «resultados.txt» 
en la lista lineas (en cada elemento de la lista se guarda una línea del archivo), eliminando los saltos de línea finales de cada línea.

"""

linea = "loquesea"
todos = ["1","2","3","4","5","6","7","8","9"]
no_estan = []
resultado = []

archivo = open("datos.txt", "r+")
while linea != '':
    linea = archivo.readline().strip()
    for x in todos:
        if x not in linea:
            no_estan.append(x)
    no_estan = sorted(no_estan)
    
    parcial = []
    
    for x in linea:
        if x == "*":
            parcial.append(no_estan[0].strip())
            no_estan.pop(0)
        else:
            parcial.append(x.strip())
    archivo1 = open("resultados.txt", "a")
    archivo1.write("".join(parcial))
    archivo1.write("\n")


    