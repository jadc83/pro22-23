"""
40. Pedir diez números enteros por teclado y mostrar la media.
"""


lista = []
while len(lista) < 10:
    lista.append(int(input("Mete numero:\n")))
media = sum(lista) / len(lista)
print(media)