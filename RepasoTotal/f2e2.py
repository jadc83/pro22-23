"""
2. La función potencia tiene la siguiente especificación:



Pre : b ≥ 0
potencia(a: int, b: int) -> int
Post : potencia(a, b) = a
b
a) Implementar la función de forma no recursiva.
b) Implementar la función de forma recursiva.

"""

potencia = lambda a, b: 1 if b == 0 else \
    a ** b
    
potencia_rec = lambda a, b: 1 if b == 0 else \
    a * potencia(a, b - 1)
    
def potencia_imp(a, b):
    return a ** b

def potencia_imp_rec(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia_imp_rec(a, b - 1) 