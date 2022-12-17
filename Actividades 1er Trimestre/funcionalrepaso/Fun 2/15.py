"""
15. La función invertir tiene la siguiente especificación:

Pre : True
invertir(t: tuple) -> tuple
Post : invertir(t) = una tupla con los elementos de t en orden contrario

Por ejemplo: invertir((1, 2, 3, 4)) == (4, 3, 2, 1).
Escribir una función recursiva que satisfaga dicha especificación

"""

invertir = lambda n: n if n == () else \
    invertir(n[1:]) + (n[0],)