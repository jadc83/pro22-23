"""
Escribir un programa que lea un archivo de texto llamado carta.txt. Tenemos que
contar los caracteres, las líneas y las palabras. Para simplificar, supondremos que cada
palabra está separada de otra por un único espacio en blanco o por un salto de línea
"""

with open("welcome.txt", "r", encoding="UTF-8") as fichero:

    LINEA = "whatever"
    LINES = 0
    chars = []
    words = []

    while LINEA != '':
        LINEA = fichero.readline()
        LINES += 1
        chars += [len(LINEA)]
        words += [len(LINEA.split())]


print(f"El archivo carta.txt tiene {LINES - 1} lineas,\
                 {sum(chars)} caracteres, {sum(words)} palabras.")
