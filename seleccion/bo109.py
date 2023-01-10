"""
109. Un anagrama es una palabra que resulta del cambio del orden de los caracteres de
otra. Ejemplos de anagramas para la palabra roma son: amor, ramo o mora. Escribir un
programa que solicite al usuario dos palabras e indique si son anagramas una de otra.
"""

palabra = input("Introduce la primera palabra:\n")
palabra2 = input("Introduce la segunda palabra:\n")
word1 = sorted(list(palabra))
word2 = sorted(list(palabra2))
if len(word1) == len(word2) and (word1 == word2):
    print("Es un anagrama")
else:
    print("No es un anagrama")