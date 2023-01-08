"""
110. Implementar el juego del anagrama, que consiste en que un jugador escribe una palabra
y el programa muestra un anagrama suyo generado al azar. A continuación, otro jugador
tiene que acertar cuál es el texto original. El programa no debe permitir que el texto
introducido por el primer jugador sea la cadena vacía. Por ejemplo, si el primer jugador
escribe «teclado», el programa muestra como pista un anagrama al azar, digamos,
«etcloda».

"""
### Imports y definiciones

import random
import os
palabra = []
contador = 10

### Empezando el turno del jugador 1

print("Turno del Jugador 1:\n")
original = input("Introduce una palabra: \n").lower()

os.system("cls")

indices = random.sample(range(0, len(original)), len(original))

for x in indices:
    palabra.append(original[x])
palabra = "".join(palabra)

### Empieza el turno del jugador 2, dentro de un bucle, hasta que acierte o agote intentos

while contador > 0:
    print(f"Turno del Jugador 2: {palabra}, intentos {contador}\n")
    intento = input("Introduce una palabra: \n").lower()
    if intento == original:
    #salida1
        print("Gana el Jugador 2!")
        input()
        break
    else:
        contador -= 1
        os.system("cls")
###Salida 2
print("Fin del juego!!")
        
