"""
3. La función repite tiene la siguiente especificación:

Pre : n ≥ 0
repite(s: str, s: int) -> str
Post : repite(s, n) = s * n
Implementar la función de forma recursiva.

"""
repite = lambda s, n: s if n <= 1 else \
    s + repite(s, (n - 1))