"""
18. La función rota1 tiene la siguiente especificación:

Pre : True
rota1(t: tuple) -> tuple
Post : rota1(t) = la tupla obtenida poniendo el primer
elemento de t al final

Por ejemplo: rota1((3, 2, 5, 7)) == (2, 5, 7, 3).
Escribir una función recursiva que satisfaga dicha especificación.

"""

rota1 = lambda t, i: t if i == 1 else \
    rota1(t[1:] + (t[0],), i + 1)