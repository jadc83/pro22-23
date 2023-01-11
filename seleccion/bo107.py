"""
107. Escribir un programa que lea una frase del teclado y nos indique si es palíndroma, es
decir, que la frase sea igual leyendo de izquierda a derecha, que de derecha a izquierda,
sin tener en cuenta los espacios ni las tildes. Por ejemplo: «Dábale arroz a la zorra el
abad».
"""

frase = input("Mete frase:\n").lower()
traduccion = frase.lower().maketrans("áéíóú","aeiou")
linea = frase.translate(traduccion).replace(" ","")

invertir = lambda c: "" if c == "" else \
    invertir(c[1:]) + c[0]
    
print(linea == invertir(linea)) 

