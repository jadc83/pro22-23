"""
66. Escribir una función a la que se le pase un número entero y devuelva el número de
divisores primos que tiene.
"""

def es_primo(n):
    if n <= 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def divisores(numero):
    contador = 0
    for x in range(1,numero + 1):
        if numero % x == 0:
            if es_primo(x):
                contador += 1
    print(f"El numero {numero} tiene {contador} divisores primos")