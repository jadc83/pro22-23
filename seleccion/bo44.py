"""
44. Pedir un número y calcular su factorial.

"""

factorial = lambda numero: 1 if numero == 0 else \
    numero * factorial(numero - 1)

def factorial_imp (numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial_imp(numero - 1)