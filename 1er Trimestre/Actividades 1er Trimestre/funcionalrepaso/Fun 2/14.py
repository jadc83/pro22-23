"""
14. La función enesimo tiene la siguiente especificación:

Pre : t ≠ () ∧ 0 ≤ n < len(t)
enesimo(n: int, t: tuple) -> Any
Post : enesimo(n, t) = el n-ésimo elemento de t

Escribir una función recursiva que satisfaga dicha especificación.

"""

enesimo = lambda a, t, i: t[0] if i == a - 1 else \
    enesimo(a, t[1:], i + 1)