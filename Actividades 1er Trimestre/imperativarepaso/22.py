"""
22. Escribir un programa que solicite al usuario el nombre de un archivo de texto y muestre
su contenido en pantalla. Si no se proporciona ningún nombre de archivo, el programa
usará por defecto prueba.txt.
"""

nombre = input("A lo que metas aqui le hago un cat\n")
contenido = open("prueba.txt")
contenido1 = open(nombre)
print(contenido.read()) if nombre == '' else print(contenido1.read())