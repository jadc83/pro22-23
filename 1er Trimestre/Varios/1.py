
letras = [ "a", "b", "d", "e", "f"]

#for i, letra in enumerate(letras):
#    print(i, letra)

lista = enumerate(letras)
mete = int(input("Mete"))
for indice, elemento in lista:
    if indice == mete - 1:
        letras.insert(indice, "c")

print(letras)