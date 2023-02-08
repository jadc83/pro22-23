"""
19. La función menor tiene la siguiente especificación:


Pre : t ≠ ()
menor(t: tuple[a]) -> a
Post : menor(t) = el menor elemento de t

Por ejemplo: menor((3, 2, 5, 7)) == 2.
Escribir una función recursiva que satisfaga dicha especificación."""

menor = lambda t: t[0] if len(t) == 1 else \
   menor(t[1:]) if t[0] > t[1] else \
      menor((t[0],) + t[1:][1])


