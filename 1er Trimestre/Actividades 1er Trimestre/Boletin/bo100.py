"""
100. Diseñar el juego «acierta la contraseña». La mecánica del juego es la siguiente: el primer
jugador introduce la contraseña sin que la vea el segundo jugador; a continuación, el
segundo jugador debe teclear palabras hasta que la acierte. El programa deberá indicar
en cada intento si la palabra introducida es mayor o menor (alfabéticamente) que la
contraseña.
"""

from getpass import getpass

password = getpass("Introduce contraseña:\n")

while True:
    intento = input("Mete intento:\n")
    if intento == password:
        print("Ganaste.")
        break
    else:
        if intento > password:
            print("Es mayor")
        else:
            print("Es menor")