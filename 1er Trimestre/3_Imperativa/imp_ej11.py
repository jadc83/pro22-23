"""
11. Escribe un programa que calcule la longitud y el Γ‘rea de una circunferencia. Para ello,
el usuario debe introducir el radio (que puede contener decimales).
Recordemos:
ππππππ‘π’π = 2π Β· πππππ
ππππ Β΄ = π Β· πππππ2

"""

from math import pi
radio = float(input('Introduce el radio:'))

longitud = (2 * pi) * radio
area = pi * (radio ** 2)

print('Longitud: ' + str(longitud))
print('Area: ' + str(area))