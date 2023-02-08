"""
119. En los sistemas Unix (como GNU/Linux) disponemos del comando more, al que se le
pasa un archivo y nos lo muestra poco a poco, cada 24 líneas. Implementar un programa
que funcione de forma similar.

"""
archivo = open("bo119.txt", "r")

while archivo.readline() != '':
    for x in range(0,6):
        print(archivo.readline())
    input("More")

archivo.close()