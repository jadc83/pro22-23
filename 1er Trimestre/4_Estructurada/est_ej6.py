"""
6. Escribir un programa que muestre por pantalla la tabla de multiplicar de un número
comprendido entre 0 y 10, introducido por teclado.

"""

numero = int(input("Introduce numero: \n"))
rango_tabla = 10
i = 0

while i <= rango_tabla:
    print(numero, "x" , i , "=" ,numero * i)
    i += 1


