"""ab = mcd(a,b) * mcm(a,b)
Se importa la funcion gcd desde el modulo math
mcd esta multiplicando, por lo que pasa hacia el otro
lado del signo = dividiendo, quedaria:

ab/mcd(a,b) = mcm(a,b) Si giramos queda mas claro
mcm(a,b) = (a*b)/mcd(a,b)

"""

from math import gcd
hola = (14*6)/gcd(14,6)
