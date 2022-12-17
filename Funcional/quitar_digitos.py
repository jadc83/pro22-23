"""
Escribir una función quitar_digitos no recursiva usando expresiones generadoras que, 
dada una cadena, la devuelva quitando todos los dígitos que puedan aparecer en ella:

quitar_digitos("hkj23hk234kj1h24kj") == "hkjhkkjhkj"

"""

quitar_digitos = lambda cadena: "".join(tuple(x for x in cadena if not x.isdigit()))