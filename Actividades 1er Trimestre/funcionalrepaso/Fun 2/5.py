"""
5. La función suma_digitos calcula la suma de los dígitos de un número entero:

suma_digitos(423) = 4 + 2 + 3 = 9
suma_digitos(7) = 7

Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.

Indicación: Recordar que n // 10 le quita el último dígito a n. Además, n % 10 devuelve
el último dígito de n.

"""

suma_digitos = lambda n: n if n < 10 else \
    n % 10 + suma_digitos( n // 10 )