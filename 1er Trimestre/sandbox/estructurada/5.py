"""
Escribir una función palindromo() que determine si una cadena es un palíndromo.

Un palíndromo es una cadena (palabra o expresión) que es igual si se lee de izquierda a derecha que de derecha a izquierda.

Por ejemplo: «Amar da drama».

La función debe ignorar los caracteres no alfabéticos y no debe distinguir las mayúsculas de las minúsculas.
"""

def palindromo(cadena):
    """palindromo"""
    cad = []
    for x in cadena:
        if x.isalpha():
            cad.append(x)
    cad1 = "".join(cad)
    return cad1.lower() == cad1[::-1].lower()