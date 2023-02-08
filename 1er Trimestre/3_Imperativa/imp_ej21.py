"""
21. Escribir un programa que duplique el contenido de un archivo cuyo nombre se pide al
usuario. El archivo copia tendrá el mismo nombre con el prefijo «copia_de_».

"""


fichero = input("Que fichero quieres copiar?\n")
newname = "copia_de_" + fichero

#################################################

origen = open("numeros_reales.txt", "r")
limpia = [ x.strip() for x in origen.readlines() ]
origen.close()

#################################################

destino = open(str(newname), "w+")

#################################################

destino.seek(0)
destino.write(str(limpia))
destino.close()