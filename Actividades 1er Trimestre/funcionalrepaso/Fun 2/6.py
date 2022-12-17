"""
6. La función voltea le da la vuelta a un número entero:

voltea(423) = 324
voltea(7) = 7

Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.

Indicación: Usar la función digitos que devuelve la cantidad de dígitos que tiene un
entero. Usar además la indicación del ejercicio anterior.

"""

digitos = lambda n: len(str(n))

voltea = lambda n: n if n < 10 else \
( (n % 10) * 10 ** (digitos(n) - 1) ) + voltea(n // 10) # ultimo digito por 10, elevado a ( n - 1 ) y se hace la rellamada con n menos ultimo digito
