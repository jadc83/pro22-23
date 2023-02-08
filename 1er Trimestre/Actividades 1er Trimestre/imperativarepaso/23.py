"""
23. Hacer el mismo ejercicio anterior, pero recogiendo el nombre del archivo desde la línea
de órdenes del sistema operativo. (Indicación: usar sys.argv).

"""

from sys import argv

if len(argv) < 2:
    contenido = open("prueba.txt")
    print(contenido.read())
else:
    contenido1 = open(argv[1])
    print(contenido1.read()) 