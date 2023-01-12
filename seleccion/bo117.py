"""
117. Crear un programa que escriba en un archivo de texto, línea a línea, 
frases introducidas por el teclado hasta que se introduzca la cadena «fin».
"""

frase = "loquesea"
while frase != "fin":
    frase = input("Mete frase:\n")
    if frase == "fin":
        break
    else:
        archivo = open("bo117.txt", "a")
        archivo.write(frase + "\n")
        archivo.close()