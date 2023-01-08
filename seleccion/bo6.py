"""
6. Un economista te ha encargado un programa para realizar cálculos con el IVA. El
programa debe solicitar la base imponible y el IVA que se debe aplicar. Muestra en
pantalla el importe correspondiente al IVA y al total.
"""

base = float(input("Introduzca base imponible:\n"))
iva = float(input("Introduce el IVA a aplicar:\n"))

tiva = round(base * (iva / 100), 2)

print(f"El IVA a aplicar es {tiva}€ y el total asciende a: {base + tiva}€")