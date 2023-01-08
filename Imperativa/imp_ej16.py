"""
16. Escribir un programa que muestre por pantalla la tabla de multiplicar de un número
comprendido entre 0 y 10, introducido por teclado.

"""

numero = int(input('Introduce numero:\n'))
acum = []
print('La tabla del ' + str(numero) )

for i in range(0,11):
    print(str(numero) + " x " + str(i) + ' = ' + str(numero * i))
    acum = acum + [i,]
    print(acum)