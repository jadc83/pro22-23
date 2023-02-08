"""
Escribir una función ahorcado(intento) que juegue un turno del juego del ahorcado. 
Para ello, la función recibe una cadena (el intento) con la palabra que el usuario
cree que es la que hay que averiguar (la solución). La solución se encuentra almacenada
en la primera línea del archivo de texto «ahorcado.txt».
 
La función deberá leer ese archivo y comprobar si el intento coincide con la solución. 
En caso afirmativo, deberá mostrar por la salida el mensaje «¡Enhorabuena!». 
En caso contrario, deberá mostrar la solución con las letras adivinadas 
(es decir, las letras que aparecen en el intento), y las letras no adivinadas 
sustituidas por un guión bajo. Se supone que las letras son siempre mayúsculas y sin acentos.

Por ejemplo, si la solución es la palabra «INFORMATICA», tenemos:

>>> ahorcado('MANZANA')
_N___MA___A
>>> ahorcado('MATEMATICAS')
I____MATICA
>>> ahorcado('INFORMATICA')
¡Enhorabuena!
"""
palabra = "INFORMATICA"

def ahorcado (cadena):
    fichero = open("ahorcado.txt", "r")
    linea = fichero.readline().strip()
    fichero.close()
    res = []
    if cadena == linea:
        print("Enhorabuena!", end = "")
    else:
        for i in linea.upper():
            if i not in cadena.upper():
                res += "_"
            else:
                res += i
    print("".join(res))