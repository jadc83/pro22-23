"""
97. Escribir un programa que solicite los elementos de una matriz de tamaño 4 × 4. La
aplicación debe decidir si la matriz introducida corresponde a un cuadrado mágico,
que es aquel en el que la suma de los elementos de cualquier fila, columna, diagonal
principal y diagonal secundaria valen lo mismo.
"""

matriz = {(0,0):1,(0,1):6,(0,2):3,(0,3):1,
          (1,0):3,(1,1):2,(1,2):7,(1,3):1,
          (2,0):1,(2,1):6,(2,2):1,(2,3):1,
          (3,0):1,(3,1):1,(3,2):1,(3,3):1}

filas = []
columnas = []
diagonal1 = []
diagonal2 = []

for c in range(0,4):
    lista = []
    lista1 = []
    for key, value in matriz.items():
        if key[0] == c:
            lista.append(value)
        if key[1] == c:
            lista1.append(value)
    filas.append(lista)
    columnas.append(lista1)

for key, value in matriz.items():
    if key[0] == key[1]:
        diagonal1.append(value)
    if (key[0] + key[1]) == 3:
        diagonal2.append(value)
        
total_filas = list(set([ sum(x) for x in filas]))[0]
total_columnas = list(set([ sum(x) for x in columnas]))[0]
total_diagonal1 = sum(diagonal1)
total_diagonal2 = sum(diagonal2)

print(total_filas == total_columnas == total_diagonal1 == total_diagonal2)