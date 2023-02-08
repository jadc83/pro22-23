"""
La función sustituye tiene la siguiente especificación:

Pre >>>> True
    sustituye(a, b, t: tuple) -> tuple
Post >>>> sustituye(a, b, t) = una tupla igual que t pero sustituyendo los a por b

Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
a) recursivo.
b) iterativo.
"""
"""Iterativa"""

sustituye = lambda a, b, t, c : c if t == () else \
    t if a == b else \
        sustituye(a, b, t[1:], (b,) + c ) if a == t[0] else \
                    sustituye(a, b, t[1:], (t[0],) + c )

sustituir = lambda a, b, t : sustituye( a, b, t, ())