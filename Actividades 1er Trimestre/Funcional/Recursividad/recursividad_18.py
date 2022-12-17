"""
18. La función rota1 tiene la siguiente especificación:

Pre : True
rota1(t: tuple) -> tuple
Post : rota1(t) = la tupla obtenida poniendo el primer
elemento de t al final

Por ejemplo: rota1((3, 2, 5, 7)) == (2, 5, 7, 3).
Escribir una función recursiva que satisfaga dicha especificación
"""

rotame = lambda n, t: t if n == 0 else rotame(0,t[1:] + (t[0],))
rota = lambda t: rotame(0,t[1:] + (t[0],))
