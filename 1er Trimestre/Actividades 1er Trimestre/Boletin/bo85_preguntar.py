"""
85. Definir la función sin_repetidos que construye y devuelve una lista de longitud apropiada, 
con los elementos de la lista original donde se han eliminado los datos repetidos
"""

def sin_repetidos(lista):
    for x in lista:
        valor = lista.count(x)
        if valor > 1:
            indice = lista.index(x)
            lista.pop(indice)
    print(lista)