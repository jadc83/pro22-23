"""
12. La función sustituye tiene la siguiente especificación:

Pre : True
sustituye(a, b, t: tuple) -> tuple
Post : sustituye(a, b, t) = una tupla igual que t pero
sustituyendo los a por b
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
a) recursivo.
b) iterativo.

"""

sustituye = lambda a, b, t, i: t if t == () else \
    (b,) + sustituye(a, b, t[1:]) if t[0] == a else (t[0],) + sustituye(a,b, t[1:])

sustituyeit = lambda a, b, t, i: i if t == () else \
    sustituyeit(a, b, t[1:],i + (b,)) if t[0] == a else sustituyeit(a,b, t[1:], i + (t[0],))