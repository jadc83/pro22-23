"""

13. La función ultimo tiene la siguiente especificación:

Pre : t ≠ ()
ultimo(t: tuple)
Post : ultimo(t) = el último elemento de t

Escribir una función recursiva que satisfaga 
dicha especificación.

"""

ultimo = lambda t : () if t == () else \
    t[0] if len(t) == 1 else ultimo(t[1:])