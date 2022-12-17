"""
24. Escribir un programa que pida al usuario su nombre y su edad. Esos datos deben
guardarse en el archivo datos.txt. Si ese archivo existe, debe añadirse al final en una
nueva línea, y en caso de no existir, debe crearse.

"""
nombre = input("Introduce tu nombre:\n")
edad = input("Introduce tu edad:\n")
fichero = open("datos.txt", "a")
fichero.write(nombre)
fichero.write(edad + "\n")
fichero.close()
