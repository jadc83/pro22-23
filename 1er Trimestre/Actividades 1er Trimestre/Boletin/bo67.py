"""
67. Diseñar la función calculadora, a la que se le pasan dos números reales (los operandos)
y qué operación se desea realizar con ellos. Las operaciones disponibles son: sumar,
restar, multiplicar o dividir. Las operaciones se especifican mediante un número: 1
para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división. La función
devolverá el resultado de la operación en forma de número real.
Indicación: Los números se codifican las operaciones disponibles se pueden representar
más adecuadamente usando constantes
"""

def calculadora(num1,num2,operador):
    if operador == 1:
        res = num1 + num2
        return res
    elif operador == 2:
        res = num1 - num2
        return res
    elif operador == 3:
        res = num1 * num2
        return res
    else:
        try:
            res = num1 / num2
            return res
        except ZeroDivisionError:
            print("No se puede dividir entre 0")