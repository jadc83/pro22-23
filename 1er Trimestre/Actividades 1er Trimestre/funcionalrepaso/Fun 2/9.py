"""
. La función elem tiene la siguiente especificación:

Pre : True
elem(e, t: tuple) -> bool
Post : elem(e, t) =

True si e está en t
False en caso contrario
Escribir una función recursiva que satisfaga dicha especificación.

"""

elem = lambda e, t: False if t == () else \
    True if t[0] == e else \
        elem(e, t[1:])