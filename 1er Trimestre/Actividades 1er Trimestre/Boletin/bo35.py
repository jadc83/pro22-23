"""
35. Codificar el juego «el número secreto», que consiste en acertar un número entre 1 y 100
(generado automáticamente). Para ello se introduce por teclado una serie de números,
para los que se indica: «mayor» o «menor», según sea mayor o menor con respecto
al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde
(introduciendo un -1).

"""

import random
numero = "loquesea"
num = random.randint(1,100)
print(num)
while numero != -1:
    numero = int(input("Introduce un numero:"))
    if numero < num:
        print("Es mayor")
    elif numero > num:
        print("Es menor")
    else:
        print("Ganaste!")
        break