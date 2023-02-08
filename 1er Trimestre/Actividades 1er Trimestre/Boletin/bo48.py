"""
48. Escribir un programa que convierta un número decimal en su representación binaria.
Hay que tener en cuenta que desconocemos cuántas cifras tiene el número que introduce
el usuario.
"""

numero = (input("Numero a convertir:\n"))
solucion = bin(int(numero))
print(solucion[1:][1:])