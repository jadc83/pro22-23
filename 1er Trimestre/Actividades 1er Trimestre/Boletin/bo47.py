"""
47. Pedir por consola un número n y dibujar un triángulo rectángulo de n elementos de
lado, utilizando para ello asteriscos (*). Por ejemplo, para n = 4:
* * * *
* * *
* *
*

"""

numero = int(input("Mete numero:\n"))
for x in reversed(range(1, numero + 1)):
    print(x * "*")