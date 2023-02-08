from math import sqrt

def suma(val1, val2):
    """Devuelve la suma de val1 y val2"""
    return val1 + val2


def resta(val1, val2):
    """Devuelve la resta de val1 y val2"""
    return val1 - val2


def multiplica(val1, val2):
    """Devuelve el producto de val1 y val2"""
    return val1 * val2


def divide(val1, val2):
    """Devuelve la division de val1 entre val2"""
    try:
        return val1 / val2
    except ZeroDivisionError:
        return "No se puede dividir entre 0"
    
    
def eleva(val1, val2):
    """Devuelve val1 elevado a val2"""
    if val2 == 0:
        return 1
    elif val2 < 0:
        return (1 / (-( val1 * val2)))
    else:
        return val1 ** val2
    
    
def raiz(val):
    """Devuelve la raiz cuadrada de val1"""
    try:
        return sqrt(val)
    except ValueError:
        return "La raiz de un numero negativo no tiene solucion real."
