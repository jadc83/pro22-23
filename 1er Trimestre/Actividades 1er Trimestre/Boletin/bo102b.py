"""
102. Diseñar un programa que pida al usuario que introduzca una frase por teclado e indique
cuántos espacios en blanco tiene. Hacer dos versiones: una recorriendo la cadena y otra
sin recorrido.
"""

frase = input("Introduce una frase:\n")

contador = frase.count(" ")
print(contador)