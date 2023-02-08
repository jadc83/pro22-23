"""
La función rota tiene la siguiente especificación:

Pre : n ≥ 0
rota(n: int, t: tuple) -> tuple
Post : rota(n, t) = la tupla obtenida poniendo los n primeros
elementos de t al final

Por ejemplo:

rota(1, (3, 2, 5, 7)) == (2, 5, 7, 3)
rota(2, (3, 2, 5, 7)) == (5, 7, 3, 2)
rota(3, (3, 2, 5, 7)) == (7, 3, 2, 5)

Escribir una función recursiva que satisfaga dicha especificación.
"""

rota = lambda a, t, i: t if i == a else \
    rota(a, t[1:] + (t[0],), i + 1)