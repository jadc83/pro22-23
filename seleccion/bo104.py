"""
104. Escribir un programa que pida el nombre completo al usuario y lo muestre sin vocales
(mayúsculas, minúsculas y acentuadas). Por ejemplo, «Álvaro Pérez» se mostraría «lvr
Prz».
"""

nombre = input("Introduce nombre:\n")
vocales = [ "aAáÁeEéÉiíIÍoóÓOuUúÚ" ]
res = []
for x in nombre:
    if x not in vocales:
        res.append(x)

print("".join(res))