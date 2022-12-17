"""
11. Escribe un programa que calcule la longitud y el área de una circunferencia. Para ello,
el usuario debe introducir el radio (que puede contener decimales).
Recordemos:
𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 = 2𝜋 · 𝑟𝑎𝑑𝑖𝑜
𝑎𝑟𝑒𝑎 ´ = 𝜋 · 𝑟𝑎𝑑𝑖𝑜2

"""

from math import pi
radio = float(input('Introduce el radio:'))

longitud = (2 * pi) * radio
area = pi * (radio ** 2)

print('Longitud: ' + str(longitud))
print('Area: ' + str(area))