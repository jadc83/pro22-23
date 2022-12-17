"""
10. La función cuantos tiene la siguiente especificación:

Pre : True
cuantos(e, t: tuple) -> int
Post : cuantos(e, t) = el número de veces que aparece e en t
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
a) recursivo.
3
b) iterativo.

"""

cuantos = lambda e, t, i: i if t == () else \
    cuantos(e, t[1:], i + 1) if t[0] == e else cuantos(e, t[1:], i)
