"""
87. Escribir la función



Pre : True
eliminar_mayores(𝑙𝑖𝑠𝑡𝑎: List[int], 𝑣𝑎𝑙𝑜𝑟: int) -> List[int]
que crea y devuelve una copia de la lista 𝑙𝑖𝑠𝑡𝑎 donde se han eliminado todos los elementos
que son mayores que 𝑣𝑎𝑙𝑜𝑟.
"""

def eliminar_mayores(valor, lista):
    resultado = []
    for x in lista:
        if x <= valor:
            resultado.append(x)
    print(resultado)