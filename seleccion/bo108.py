"""
108. Se dispone de las siguientes secuencias de caracteres:
• Secuencia 1: e i k m p q r s t u v
• Secuencia 2: p v i u m t e r k q s
Con ellas, es posible codificar un texto convirtiendo cada letra de la secuencia 1 en
su correspondiente de la secuencia 2. El resto de los caracteres no se modifican. Las
secuencias se utilizan tanto para codificar mayúsculas como minúsculas, mostrando
siempre la codificación en minúsculas.
Por ejemplo, la palabra «PaquiTo» se codifica como «matqvko».
Escribir un programa que codifique un texto. Para ello, se debe implementar la siguiente
función:

Pre : len(c) = 1
codifica(sec1: str, sec2: str, c: str) -> str
Post : len(codifica(sec1, sec2, c)) = 1 ∧
c ∈ sec1 → codifica(sec1, sec2, c) = el correspondiente de c en sec2
c ∉ sec1 → codifica(sec1, sec2, c) = c
"""
sec1 = ["e", "i", "k", "m", "p", "q", "r", "s", "t", "u", "v"]
sec2 = ["p", "v", "i", "u", "m", "t", "e", "r", "k", "q", "s"]
resultado = []
def codifica(sec1,sec2,c):
    sec11 = list(enumerate(sec1,0))
    sec22 = list(enumerate(sec2,0))
    if c in sec1:
        indice = sec1.index(c)
        cc = sec22[indice]
        return cc[1]
    else:
        return c
codificada = input("Inserta texto a codificar:\n")
for x in codificada:
    resultado.append(codifica(sec1,sec2,x))
resultado = "".join(resultado)

print(f"Salida: {resultado}")

