"""
15. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
joven!» si es menor de 25 años, «No está mal.» si tiene entre 25 y 40 años y «¡Qué
mayor!» si tiene más de 40 años.
"""

edad = int(input("Que edad tienes?\n"))

print("Que joven!") if edad < 25 else \
    print("No esta mal") if edad >= 25 and edad <= 40 else \
        print("Que mayor!")