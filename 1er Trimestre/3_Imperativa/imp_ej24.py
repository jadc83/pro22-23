"""
24. Escribir un programa que pida al usuario su nombre y su edad. Esos datos deben
guardarse en el archivo datos.txt. Si ese archivo existe, debe añadirse al final en una
nueva línea, y en caso de no existir, debe crearse.

"""

nombre = input('Introduce tu nombre: ')
edad = input('Introduce tu edad: ')

archivo = open('nombres.txt', "a")
write1 = archivo.write(nombre)
write2 = archivo.write('#')
write3 = archivo.write(edad)
write4 = archivo.write("\n")
archivo.seek(0)
archivo.close()