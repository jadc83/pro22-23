"""
11. Escribir un programa que determine si un número entero introducido por teclado es
primo o compuesto.
Indicación: Un número primo es aquel que sólo puede dividirse exactamente por sí
mismo y por 1.
"""
n = int(input("Mete numero:\n"))
i = 0

for x in range(1, n+1):
    if n % x == 0:
        i += 1

if i == 2:
    print("Es primo")
else:
    print("Es compuesto")
