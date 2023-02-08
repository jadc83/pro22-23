from math import sqrt

###SUMA###
def suma(val1, val2):
    """Devuelve la suma de val1 y val2"""
    try: return val1 + val2
    except TypeError: return "Esta no es la funcion concatenar"

###RESTA###
def resta(val1, val2):
    """Devuelve la resta de val1 y val2"""
    try: return val1 - val2
    except TypeError: return "No se aceptan letras"

###MULTIPLICA###
def multiplica(val1, val2):
    """Devuelve el producto de val1 y val2"""
    try: return val1 * val2
    except TypeError: return "No se aceptan letras"
    
###DIVIDE###
def divide(val1, val2):
    """Devuelve la division de val1 entre val2"""
    try: return val1 / val2
    except ZeroDivisionError: return "No se puede dividir entre 0"
    except TypeError: return "No se puede dividir entre una letra"
    
###ELEVA###
def eleva(val1, val2):
    """Devuelve val1 elevado a val2"""
    try:
        if val2 == 0: return 1
        elif val2 < 0: return (1 / (-( val1 * val2)))
        else: return val1 ** val2
    except TypeError: return "No se puede elevar a una letra"
    
###RAIZ###
def raiz(val):
    """Devuelve la raiz cuadrada de val1"""
    try: return sqrt(val)
    except ValueError:return "La raiz de un numero negativo no tiene solucion real."
    except TypeError: return "No se puede hacer la raiz cuadrada a una letra"
