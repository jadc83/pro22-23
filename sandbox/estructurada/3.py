"""
Escribir una función hamming() que calcule la distancia Hamming entre dos cadenas,

La distancia Hamming entre dos cadenas se calcula comparando las dos cadenas y contando cuántos de sus caracteres son distintos a los de sus equivalentes en la otra cadena:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
La distancia Hamming entre esas dos cadenas de es 7.

Importante: sólo se puede calcular la distancia Hamming entre dos cadenas de igual longitud.
"""
"""hamming"""
def hamming(cad1, cad2):
    lista1 = []
    lista2 = []
    res = 0
    for x in cad1:
        lista1.append(x)
    for x in cad2:
        lista2.append(x)
    lista = list(zip(lista1,lista2))
    
    for x, y in lista:
        if x != y:
            res += 1
    return res