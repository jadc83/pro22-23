"""
111. Modificar el programa anterior para que indique al segundo jugador cuántas letras
coinciden (son iguales y están en la misma posición) entre el texto introducido por él y
el original.
"""

### Imports y definiciones

import random
import os
import getpass #getpass se usa para esconder passwords, aqui nos vale para ocultar la palabra
palabra = []
lista2 = []
contador = 10

#############################JUGADOR 1##################################
print("Turno del Jugador 1:")
adivina = getpass.getpass(prompt='Introduce la palabra: ', stream=None) 
os.system("cls")

indices = random.sample(range(0, len(adivina)), len(adivina))
for x in indices:
    palabra.append(adivina[x])
palabra = "".join(palabra)
#############################JUGADOR 2##################################
while contador > 0:
    print(f"Turno del Jugador 2: {palabra}, intentos {contador}\n")
    intento = input("Introduce una palabra: \n").lower()
    if intento == adivina:
        print("Gana el Jugador 2!")
        input()
        break
    else:
        contador -= 1
        for x in adivina:
            if x in intento:
                lista2.append(x)
            else:
                lista2.append("_")
        lista2 = "".join(lista2)
        print(f"Tu intento: {lista2} ")
        input()
        lista2 = []
        os.system("cls")