"""
21. Escribir un programa que duplique el contenido de un archivo cuyo nombre se pide al
usuario. El archivo copia tendrá el mismo nombre con el prefijo «copia_de_».
"""

filename = input("Introduzca el nombre del fichero a copiar:\n")
fichero = open(filename, "r")
fichero2 = open("copia_de_" + filename, "w")
linea = "loquesea"
while linea != '':
    linea = fichero.readline()
    print(linea, file=fichero2, end="")
fichero.close()
fichero2.close()