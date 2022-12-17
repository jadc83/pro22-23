"""
8. Escribir un programa que calcule la media de cinco valores numéricos reales (tipo float)
introducidos por teclado.

"""
cont = 0
i = 0
while cont < 5:
    num = float(input("Introduce valor:"))
    i = i + num
    cont = cont + 1
print(i / cont)



