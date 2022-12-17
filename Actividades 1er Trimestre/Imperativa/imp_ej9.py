"""
9. Escribe un programa que solicite al usuario un número y le indique si es par (mediante
un mensaje Sí o No).

"""


numero = int(input('Introduce numero:\n'))


check = 'Si' if numero % 2 == 0 else 'No'
print(check)