"""
37. Desarrollar un juego que ayude a mejorar el cálculo mental de la suma. 

El jugador tendrá que introducir la solución de la suma de dos números aleatorios comprendidos
entre 1 y 100. Mientras la solución introducida sea correcta, el juego continuará. 

En caso contrario, el programa terminará y mostrará el número de operaciones realizadas
correctamente
"""

import random
import time
import signal

contador = 0

while True:
    num1 = random.randint(1,101)
    num2 = random.randint(1,101)
    compara = num1 + num2
    print(num1, num2)
    intento = int(input("Resultado:\n"))
    if intento == compara:
        contador += 1
    else:
        print("Fallo!")
        print(f"{contador} aciertos.")
        break
