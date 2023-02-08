"""
112. Escribir un programa que lea del teclado una frase e indique, para cada carácter que
aparece en la frase, cuántas veces aparece. Se consideran iguales las letras mayúsculas
y minúsculas para realizar la cuenta. Por ejemplo:
Frase: En un lugar de La Mancha.
Resultado:
a: 4 veces
c: 1 vez
d: 1 vez
e: 2 veces
...

"""

frase = input("Introduce frase: \n")

for e in frase:
    print(f"{e}: {frase.count(e)} veces")