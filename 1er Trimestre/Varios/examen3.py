"""
Escribir una función diferencia_diagonales(matriz)
que reciba una matriz cuadrada
(mismo número de filas que de columnas) y que devuelva
la diferencia (en valor absoluto)
de las sumas de sus diagonales.

Importante: La matriz debe venir codificada en forma de diccionario,
donde las claves serán tuplas (fila, columna) empezando a contar
desde 0, y los valores serán los enteros que forman la matriz.
Así, en la matriz del ejemplo, su diccionario correspondiente
contendrá el elemento (1, 2): 6.
"""

matriz = [ [(0,0), 6],[(0,1), 5],[(0,2), 9],
           [(1,0), 2],[(1,1), 3],[(1,2), 1],
           [(2,0), 8],[(2,1), 6],[(2,2), 6]]

matriz1 = { (0,0):5, (0,1):5, (0,2):5,
            (1,0):5, (1,1):5, (1,2):5,
            (2,0):5, (2,1):5, (2,2):5 }

def diferencia_diagonales(matriz):    
    diag1 = matriz[0][1] + matriz[4][1] + matriz[8][1] #15
    diag2 = matriz[2][1] + matriz[4][1] + matriz[6][1]
    return diag1 - diag2

for x in matriz1:
    print(x,x,x)
