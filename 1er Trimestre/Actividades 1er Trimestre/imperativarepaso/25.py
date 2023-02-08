"""
 Escribir un programa que lea dos listas de números enteros no ordenados de sendos
archivos con un número por línea, los reúna en una lista única y los guarde en orden
creciente en un tercer archivo, de nuevo uno por línea.
"""

file1 = open("file1.txt", "r")
linea1 = file1.readlines()
linea11 = [int(x.strip()) for x in linea1]
file1.close()

file2 = open("file2.txt", "r")
linea2 = file2.readlines()
linea22 = [int(x.strip()) for x in linea2]
file2.close()

linea3 = sorted(linea11 + linea22)

final = [str(x) + "\n" for x in linea3]

file3 = open("file3.txt", "a")
file3.writelines(final)
file3.close()