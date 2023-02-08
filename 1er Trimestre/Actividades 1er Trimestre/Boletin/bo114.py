"""
114. Escribir un programa que pida un entero por la consola, leyéndolo del teclado, y lo
imprime. Si la cadena introducida por consola no tiene el formato correcto, muestra un
mensaje de error y vuelve a pedirlo
"""

while True:
    try:
        numero = int(input("Introduce numero:\n"))
        print(numero)
        break
    except ValueError:
        print("No cumple con la condicion.")