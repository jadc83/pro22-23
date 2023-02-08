"""
22. La función finales tiene la siguiente especificación:

Pre : n ≥ 0
finales(n: int, t: tuple) -> tuple
Post : finales(n, t) = la tupla que contiene los n elementos finales de n
Por ejemplo: finales(2, (1, 2, 3, 4)) == (3, 4).
Escribir una función recursiva que satisfaga dicha especificación.

rota = lambda n, t: t if n == 0 else rota(0,t[n:] + t[:n]) esta funcion devuelve los n-primeros
y necesito los n-finales

"""

#finales = lambda n, t: t if n == 0 else finales(0,invertir(invertir(t)[:n]))

finales = lambda n, t: t if len(t) == n else finales(n,t[1:])

insertar = lambda num, pos, tupla: t if num == 0 else \
    