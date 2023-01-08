"""
Escribir una función isograma() que determine si una palabra o frase es un isograma.

Un isograma es una palabra o frase que no tiene ninguna letra repetida.

Ejemplos de isogramas:

camino
campeón
mutación
La función debe devolver True si la cadena introducida es un isograma, o False en caso contrario.

Importante: Los espacios en blanco se ignoran, y la función no debe distinguir las letras mayúsculas de las minúsculas.

Por ejemplo:
"""
"isograma"
def isograma(cadena):
    for x in cadena.split(" "):
        if cadena.lower().count(x) > 1:
            return False
    return True
