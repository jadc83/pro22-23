"""
14. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
joven!» si es menor de 25 años y «No está mal.» si tiene entre 25 y 40 años.

"""

edad = int(input('Que edad tienes?:\n'))

check = 'Que joven!' if edad < 25 else \
              'No esta mal' if edad >= 25 and edad <= 40 else '' 
    
print(check)