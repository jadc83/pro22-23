"""
65. Implementar la función definida según la siguiente especificación:

Pre : n ≥ 0
es_primo(n: int) -> bool
Post : es_primo(n) = True si n es primo False en caso contrario
"""

def es_primo(n):
    if n <= 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True