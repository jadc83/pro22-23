"""
1. Implementar un programa que pida al usuario un número comprendido entre 1 y
10. Hay que mostrar la tabla de multiplicar de dicho número, asegurándose de que el
número introducido se encuentra en el rango establecido.
"""
def tabla(numero):
        if numero < 1 or numero > 10:
            print("El numero no es correcto.")
        else: 
            for x in range(1, 11):
                print(f"{numero} por {x} es {numero * x}")