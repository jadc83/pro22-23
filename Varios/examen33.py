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

#Recordartorio, usar una matriz para simular un tablero puede ser una buena idea
"""
matriz = {((0,0), 6), ((0,1), 4), ((0,2), 46), ((0,3), 6), ((0,4), 461),
          ((1,0), 4), ((1,1), 6), ((1,2), 61), ((1,3), 5), ((1,4), 46),
          ((2,0), 6), ((2,1), 6), ((2,2), 54), ((2,3), 101), ((2,4), 4),
          ((3,0), 13), ((3,1), 9), ((3,2), 41), ((3,3), 99), ((3,4), 46),
          ((4,0), 4), ((4,1), 6), ((4,2), 46), ((4,3), 54), ((4,4), 436)} 

def diferencia_diagonales ( matriz ):
    from math import sqrt

    matrix = dict(matriz)
    filas = sqrt(len(matrix)) #Este sera el largo y ancho

    diag1 = 0
    for a, b in matrix:
        if a == b:
            diag1 += matrix[a,b]
    diag2 = 0
    for a, b in matrix:
        if a + b == 2:
            diag2 += matrix[a,b]
    print(diag1-diag2)
