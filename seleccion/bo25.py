"""
25. Escribir un programa que indique cuántas cifras tiene un número entero introducido
por teclado, que estará comprendido entre 0 y 99 999.

"""

numero = int(input("Introduce numero:\n"))
copia = numero
contador = 0
while copia != 0:
    copia = copia // 10
    contador += 1

if contador == 0:
    print(1)
else:
    print(contador)