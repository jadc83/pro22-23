"""
90. Desarrollar el juego «la cámara secreta», que consiste en abrir una cámara mediante su
combinación secreta, que está formada por una combinación de dígitos del 1 al 5. El
jugador especificará cuál es la longitud de la combinación; a mayor longitud, mayor
será la dificultad del juego. La aplicación genera, de forma aleatoria, una combinación
secreta que el usuario tendrá que acertar. En cada intento se muestra como pista, para
cada dígito de la combinación introducido por el jugador, si es mayor, menor o igual
que el correspondiente en la combinación secreta.

"""
import random

numeros = [1,2,3,4,5]
longitud = int(input("Introduce longitud de la combinacion:\n"))
codigo = random.choices(numeros, k=longitud)

intento = []
for x in range(1, longitud + 1):
    intento.append(int(input("Introduce tu intento:\n")))
    
compara = list(zip(codigo, intento))
resultado = []

for x,y in compara:
    if x == y:
        resultado.append(x)
    if y < x:
        resultado.append("-")
    if y > x:
        resultado.append("+")

print("".join(resultado))