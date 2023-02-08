
"""
Escribir un programa que juegue con el usuario a que éste tiene que adivinar un número del 0 al 99.

El programa debe «pensar» un número de forma aleatoria usando la función random.randint().

A continuación, debe pedir al usuario que introduzca un numero diciendo «Introduce un número: » (cuidado con los espacios).

Si el número es el que había pensado, debe decir «¡Acertaste!» y finalizar el programa.
Si el número es menor que el que había pensado, debe decir «Es demasiado pequeño.» y pedir de nuevo otro número.
Si el número es mayor que el que había pensado, debe decir «Es demasiado grande.» y pedir de nuevo otro número.
"""
from random import randint
numero = randint(0,99)
respuesta = "loquesea"


while numero != respuesta:
    respuesta = int(input("Introduce un número: "))
    if respuesta == numero:
        print(f"¡Acertaste!")
    else:
        if respuesta < numero:
            print(f"Es demasiado pequeño.")
        elif respuesta > numero:
            print(f"Es demasiado grande.")