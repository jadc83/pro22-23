"""
60. Escribir una función a la que se le pasen dos enteros y muestre todos los números
comprendidos entre ellos.
"""

def entre(num1,num2):
    if num1 < num2:
        for x in range(num1,num2 + 1):
            print(x)
    elif num1 == num2:
        return None
    else:
        for x in reversed(range(num2, num1 + 1)):
            print(x)