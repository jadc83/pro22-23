"""
42. Diseñar un programa que muestre las tablas de multiplicar del 1 al 10.
"""

def tabla(numero):
    if numero < 1 or numero > 10:
        print("El numero no es correcto.")
    else: 
        for x in range(1, 11):
            print(f"{numero} por {x} es {numero * x}")
        
for x in range(1,11):
    tabla(x)
    print("-----------------")