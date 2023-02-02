"""
96. Escribir la función:



Pre : True
suma(𝑙𝑖𝑠𝑡𝑎: List[int], 𝑛𝑢𝑚_𝑒𝑙𝑒𝑚: int) -> List[int]
11
que crea y devuelve una lista con las sumas de los 𝑛𝑢𝑚_𝑒𝑙𝑒𝑚 elementos consecutivos
de 𝑙𝑖𝑠𝑡𝑎.
Por ejemplo, sea 𝑙𝑖𝑠𝑡𝑎 = [10, 1, 5, 8, 9, 2]. Si los elementos de 𝑙𝑖𝑠𝑡𝑎 se agrupan de
3 en 3, se harán las sumas:
• 10 + 1 + 5 = 16.
• 1 + 5 + 8 = 14.
• 5 + 8 + 9 = 22.
• 8 + 9 + 2 = 19.
Por lo tanto, la función devolverá la lista [16, 14, 22, 19].
"""

def num_elem(lista, entero):
    "dasdasd"
    resultado = []
    while len(lista) >= entero:
        res = sum(lista[:entero])
        resultado.append(res)
        lista.pop(0)
    return resultado