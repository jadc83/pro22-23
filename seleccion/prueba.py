archivo = open("bo119.txt", "r")

contenido = "loquesea"

while contenido != '':
    for x in range(1,6):
        contenido = archivo.readline()
        print(contenido, end="")
    input(">>>>>>>>>")
