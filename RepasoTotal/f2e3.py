"""
3. La función repite tiene la siguiente especificación:



Pre : n ≥ 0
repite(s: str, n: int) -> str
Post : repite(s, n) = s * n
Implementar la función de forma recursiva

"""

repite = lambda s, n: "" if n == 0 else \
    s * n

repite_rec = lambda s, n: "" if n <= 0 else \
    "s" + repite_rec(s, n - 1)
    
def repite_imp(letra, numero):
    return letra * numero

def repite_imp_rec(letra, numero):
    if numero == 0:
        return ""
    else:
        return letra + repite_imp_rec(letra, numero - 1)