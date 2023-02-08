"""
1. Considérese la siguiente fórmula (debida a Herón de Alejandrı́a), que expresa el valor de la super‐
ficie S de un triángulo cualquiera en función de sus lados, a, b y c:

Escribir una función que obtenga el valor S a partir de a, b y c, evitando el cálculo repetido del
semiperı́metro, sp =
(a+b+c) / 2
, y almacenando el resultado finalmente en la variable S.

"""
from math import sqrt
def heron (a, b,c):
    sp = ( a + b + c) / 2
    S = sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    return S

