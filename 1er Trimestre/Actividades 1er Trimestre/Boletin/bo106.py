"""
106. Introducir por teclado una frase palabra a palabra, y mostrar la frase completa separando
las palabras introducidas con espacios en blanco. Terminar de leer la frase cuando alguna
de las palabras introducidas sea la cadena «fin» esritsa con cualquier combinación de
mayúsculas y minúsculas. La cadena «fin» no aparecerá en la frase final.
"""
palabra = "loquesea"
frase = []
while palabra != "fin":
    palabra = input("Introduce palabra:").lower()
    if palabra == "fin":
        break
    else:
        frase.append(palabra)
print(" ".join(frase))
    