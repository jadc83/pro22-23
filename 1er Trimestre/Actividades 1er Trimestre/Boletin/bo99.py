"""
99. Introducir por teclado dos frases e indicar cuál de ellas es la más corta, es decir, la que
tiene menos caracteres.

"""
frase1 = input("Mete frase 1:\n")
frase2 = input("Mete frase 2:\n")

if len(frase1) > len(frase2):
    print("La primera es mayor")
elif len(frase2) > len(frase1):
    print("La segunda es mayor.")