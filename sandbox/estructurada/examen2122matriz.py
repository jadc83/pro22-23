"""
MAtrices examen 2122 python
"""
def diferencia_diagonales(matriz):
    """diferencia matrices"""
    diag1 = 0
    diag2 = 0

    for key, value in matriz.items():
        if key[0] == key[1]:
            diag1 += value
        
    for key, value in matriz.items():
        if key[0] + key[1] == 2:
            diag2 += value
        
    return abs(diag1 - diag2)