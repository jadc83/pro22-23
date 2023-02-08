"""
8. Modifica el ejercicio anterior para que, indicando dos números n y m, diga qué cantidad
hay que sumarle a n para que sea múltiplo de m.
"""

numero1 = int(input("Mete numero:\n"))
numero2 = int(input("Mete otro numero:\n"))
cifra1 = numero1
cifra2 = numero2
contador = 0
while cifra1 % cifra2 != 0:
    cifra1 += 1
    contador += 1
print(f"{numero1} + {contador} es multiplo de {numero2} ({numero1 + contador})")