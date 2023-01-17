"""
89. El «número de la suerte» de una persona se puede calcular a partir de sus números
favoritos. De entre ellos, se seleccionan dos diferentes al azar, que se eliminarán de la
lista, pero en su lugar se añade la media aritmética de los dos eliminados a la lista de
números favoritos. El proceso se repite hasta que sólo quede un número, que resultará
el número de la suerte para esa persona.
Escribir un programa que solicite al usuario sus números favoritos y calcule su número
de la suerte
"""

numeros = []

while True:
    valor = int(input("Mete numero: \n"))
    if valor >= 0:
        numeros.append(valor)
    else:
        break

numerosbak = numeros    
numeros = set(numeros)

while len(numeros) != 1:
    aleatorio1 = numeros.pop()
    aleatorio2 = numeros.pop()
    numeros.add((aleatorio1 + aleatorio2) / 2)
    
resultado = list(numeros)
print(int(resultado[0]))


