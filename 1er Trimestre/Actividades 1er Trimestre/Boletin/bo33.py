"""
33. Escribir un programa que muestre, para cada número introducido por teclado, si es par,
si es positivo y su cuadrado. El proceso se repetirá hasta que se introduzca un 0.
"""
numero = "loquesea"

def espar(numero):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "Es impar"
def positivo(numero):
    if numero > 0:
        return "Es positivo"
    else:
        return "Es negativo"
def cuadrado(numero):
    return numero ** 2

while numero != 0:
    numero = int(input("Mete numero: \n"))
    if numero == 0:
        break
    else:
        print(f"{espar(numero)}, {positivo(numero)} y su cuadrado es {cuadrado(numero)}")
        input()