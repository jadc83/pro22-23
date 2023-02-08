"""
16. Escribir un programa que muestre por pantalla la tabla de multiplicar de un número
comprendido entre 0 y 10, introducido por teclado.
"""
num = int(input("Mete numer:\n"))

i = 0

while i < 11:
    print(f"{num} por {i} es {num * i}")
    i += 1
