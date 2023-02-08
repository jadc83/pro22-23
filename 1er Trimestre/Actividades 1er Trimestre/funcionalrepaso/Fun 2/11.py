"""
11. La función quita tiene la siguiente especificación:

Pre : True
quita(e, t: tuple) -> tuple
Post : quita(e, t) = una tupla igual que t pero sin los e

Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:

a) recursivo.
b) iterativo.

"""

quita = lambda e, t: () if t == () else \
    (t[0],) + quita(e, t[1:] ) if t[0] != e else quita(e, t[1:])

quitait = lambda e, t, i: i if t == () else \
    quitait(e, t[1:], i + (t[0],) ) if t[0] != e else quitait(e, t[1:], i)