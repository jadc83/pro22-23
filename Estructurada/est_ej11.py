
"""
11. Escribir un programa que determine si un número entero introducido por teclado es
primo o compuesto.
Indicación: Un número primo es aquel que sólo puede dividirse exactamente por sí
mismo y por 1.
"""

numero = int(input("Número: "))
contador = numero
acumulador = 0

while contador >= 1:
    if numero % contador == 0:
        acumulador += 1
        contador -= 1
    else:
        contador -= 1

def es_primo(acumulador):
    if acumulador == 2:
         return "Es primo"
    else:
         return "Es compuesto"

print(es_primo(acumulador))