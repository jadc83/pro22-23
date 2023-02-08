"""
21. Implementar un programa que pida por teclado un número decimal e indique si es un
número casi-cero, que son aquellos números (positivos o negativos) que se acercan a
cero por menos de 1 unidad (aunque, curiosamente, el 0 no se considera un número
casi-cero). Ejemplos de números casi-cero son el 0.3, el −0.99 o el 0.123. En cambio,
algunos números que no se consideran casi-cero son 12.3, el 0 o el −1.
"""

numero = float(input("Introduce numero: \n"))

if abs(numero) > 0 and abs(numero) < 1:
    print("Lo es")
else:
    print("No lo es")