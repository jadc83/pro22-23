"""
13. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
joven!» si es menor de 25 años y «¡Qué mayor!» en caso contrario.

"""

edad = int(input('Que edad tienes?:\n'))

check = 'Que joven!' if edad < 25 else 'Que mayor!'
print(check)