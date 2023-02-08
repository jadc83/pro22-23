"""
8. Escribir un programa que calcule la media de cinco valores numéricos reales (tipo float)
introducidos por teclado.

"""

i = 0
lista = []

while i != 5:
    lista.append(float(input("Mete numero:\n")))
    i += 1

print(f"La media de {tuple(lista)} es {sum(lista) / len(lista)}")