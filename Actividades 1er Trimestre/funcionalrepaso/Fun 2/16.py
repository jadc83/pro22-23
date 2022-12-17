"""
16. La función palindromo tiene la siguiente especificación:

Pre : True
palindromo(t: tuple) -> bool
Post : palindromo(t) = bool

True si t es un palíndromo
(se lee igual en un sentido que en otro)
False en caso contrario
Por ejemplo: palindromo((1, 2, 3, 4, 3, 2, 1)) == True.
Escribir una función recursiva que satisfaga dicha especificación.

"""
invertir = lambda n: n if n == () else \
    invertir(n[1:]) + (n[0],)

palindromo = lambda t: True if len(t) <= 1 else \
    palindromo(t[1:]) if t[0] == invertir(t[0]) else False
    

