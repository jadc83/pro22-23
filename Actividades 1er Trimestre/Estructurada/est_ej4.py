"""
4. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
joven!» si es menor de 25 años y «No está mal.» si tiene entre 25 y 40 años.

"""

edad = int(input("¿Qué edad tienes?\n"))

if edad < 25:
    print("¡Qué joven!")

elif edad in range(24,41):
    print("No está mal")

else:
    print("", end = "")