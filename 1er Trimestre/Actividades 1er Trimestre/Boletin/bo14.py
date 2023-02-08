"""
14. Una empresa que gestiona un parque acuático te solicita un programa que les ayude
a calcular el importe que hay que cobrar en la taquilla por la compra de una serie de
entradas (cuyo número será introducido por el usuario). Existen dos tipos de entrada:
infantil, que cuestan 15.50 €; y de adultos, que cuestan 20 €.
En el caso de que el importe total sea igual o superior a 100 €, se aplicará automáticamente un bono descuento del 5 %
"""

adulto = int(input("Entradas de adulto:\n"))
niño = int(input("Entradas de niño:\n"))

p1 = (adulto * 20) + (niño * 15.50)
p2 = p1 - ( ((adulto * 20) + (niño * 15.50)) * 0.05 )

if p1 < 100:
    print(p1)
else:
    print(p2)