import re
linea = "loquesea"
patron = re.compile('D[a-z0-9]+')
contador = 0
archivo = open("bo115.txt", "r")
while linea != "":
    linea = archivo.readline()
    var2 = patron.findall(linea)
    print("".join(var2))