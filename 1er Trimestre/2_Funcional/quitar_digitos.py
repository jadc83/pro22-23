"""
Escribir una función quitar_digitos no recursiva usando expresiones generadoras que, 
dada una cadena, la devuelva quitando todos los dígitos que puedan aparecer en ella:

quitar_digitos("hkj23hk234kj1h24kj") == "hkjhkkjhkj"

"""

quitar_digitos = lambda cadena: "".join(tuple(x for x in cadena if not x.isdigit()))


"""Escribir una función quitar_digitos recursiva que dada una cadena, 
   la devuelva quitando todos los dígitos que puedan aparecer en ella:

    quitar_digitos("hkj23hk234kj1h24kj") == "hkjhkkjhkj
"""

quitar_digitos_rec = lambda cadena, acumulador: "".join(acumulador) if cadena == "" else \
    quitar_digitos_rec(cadena[1:], acumulador + (cadena[0],)) if cadena[0].isalpha() else \
        quitar_digitos_rec(cadena[1:], acumulador)
        
"""Escribir una función quitar_digitos usando funciones de orden superior que dada una cadena, 
   la devuelva quitando todos los dígitos que puedan aparecer en ella:

    quitar_digitos("hkj23hk234kj1h24kj") == "hkjhkkjhkj
"""

isletra = lambda x: x.isalpha()

quitar_digitos_os = lambda cadena:  "".join(list(filter(isletra,cadena)))