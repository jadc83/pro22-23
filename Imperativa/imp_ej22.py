""""
22. Escribir un programa que solicite al usuario el nombre de un archivo de texto y muestre
su contenido en pantalla. Si no se proporciona ningún nombre de archivo, el programa
usará por defecto prueba.txt.

"""

nombre = lambda a: 'pruebas.txt' if a == '' else filename
filename = input("Introduzca nombre del fichero:")

#############################################################

fichero = open(nombre(filename), "r")
copiando = fichero.readlines()
fichero.close()

#############################################################

limpiando = [x.strip() for x in copiando]
dale = [print(x) for x in limpiando]











