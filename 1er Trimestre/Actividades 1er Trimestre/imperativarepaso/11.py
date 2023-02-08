"""
11. Escribe un programa que calcule la longitud y el área de una circunferencia. Para ello,
el usuario debe introducir el radio (que puede contener decimales).
Recordemos:
longitud = 2𝜋 · r
area = 𝜋 · r ** 2

"""

from math import pi
radio = float(input("Introduce radio:\n"))
longitud = (2 * pi) * radio
area = pi * (radio ** 2)

print(f"La longitud es {round(longitud,2)} y el area es {round(area,2)}")