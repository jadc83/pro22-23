"""
8. Escribe un programa que solicite al usuario su edad y le indique si es mayor de edad
(mediante un mensaje Sí o No).

"""

edad = input('Introduce edad:\n')


check = 'Si' if int(edad) >= 18 else 'No'
print(check)