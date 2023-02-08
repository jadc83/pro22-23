"""
a. Pedir los dos términos de una fracción y dar el valor de la división correspondiente, a no ser
que sea nulo el hipotético denominador, en cuyo caso se avisará del error.

"""

numerador = int(input("Numerador: \n"))
denominador = int(input("Denominador: \n"))

try:
    print(numerador / denominador)
except ZeroDivisionError:
    print("Division entre 0 no permitida")