"""
92. Escribir la función:



Pre : True
buscar_todos(𝑙𝑖𝑠𝑡𝑎: List[int], 𝑐𝑙𝑎𝑣𝑒: int) -> List[int]

que crea y devuelve una lista con todos los índices de los elementos donde se encuentra
la clave de búsqueda 𝑐𝑙𝑎𝑣𝑒. En el caso de que 𝑐𝑙𝑎𝑣𝑒 no se encuentre en 𝑙𝑖𝑠𝑡𝑎, la función
devolverá una lista vacía.

"""

def buscar_todos(lista, clave):
    indices = []
    for x, y in enumerate(lista):
        if y == clave:
            indices.append(x)
    print(indices)
