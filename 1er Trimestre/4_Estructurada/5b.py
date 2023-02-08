"""
b. Pedir los coeficientes de una ecuación de segundo grado y dar las dos soluciones correspon‐
dientes, comprobando previamente si el discriminante es positivo o no.

discriminante = pow( b, 2 ) - 4 * a * c ))) 
"""
from math import sqrt

a = int(input("Coeficiente 1: \n"))
b = int(input("Coeficiente 2: \n"))
c = int(input("Coeficiente 3: \n"))

try:

    disc = sqrt(pow( b, 2 ) - 4 * a * c )
    arriba1 = (-b - disc ) / (2 * a) 
    arriba2 = (-b + disc ) / (2 * a)
    print(arriba1, arriba2)

except ValueError:
    print("Error, El discriminante no es positivo.")