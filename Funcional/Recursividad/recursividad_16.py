"""
16. La función palindromo tiene la siguiente especificación:

Pre : True
palindromo(t: tuple) -> bool
Post : palindromo(t) =

True si t es un palíndromo
(se lee igual en un sentido que en otro)
False en caso contrario

Por ejemplo: palindromo((1, 2, 3, 4, 3, 2, 1)) == True.
Escribir una función recursiva que satisfaga dicha especificación.
"""

invierteSTR = lambda c: "" if c == "" else \
    invierteSTR(c[1:]) + (c[0])
palindromoC = lambda a: True if a == invierteSTR(a) else False


invertirTUP = lambda t: () if t == () else \
    invertirTUP(t[1:]) + (t[0],)
palindromoT = lambda a: True if a == invertirTUP(a) else False