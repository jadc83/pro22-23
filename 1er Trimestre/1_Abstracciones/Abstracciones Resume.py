"""
   altura(Tamaño de tibia en cm, Sexo[ 'hombre' | 'mujer' ], Edad)
   altura(38.65, 'mujer', 30)
"""

altura = lambda tibia, sexo, edad : \
( 69.089 + ( 2.232 * tibia) ) if ( sexo == 'hombre' and edad <= 30 ) else \
( 69.089 + ( 2.232 * tibia) - ((edad - 29) * 0.06)) \
if ( sexo == 'hombre' and edad > 30) else \
( 61.412 + ( 2.317 * tibia) ) if ( sexo == 'mujer' and edad <= 30 ) else \
( 61.412 + ( 2.317 * tibia) - ((edad - 29) * 0.06)) \
if sexo == 'mujer' and edad > 30 else ""

"""
Volumen
from math import pi
v = ( 4 / 3 ) * ( pi * ( r ** 3 ) )
"""
from math import pi
volumen = lambda r: 'r no puede ser 0' if r <= 0 else round(( 4 / 3 ) * ( pi * ( r ** 3 )), 3)

"""
Compara
a = 1
b = 1
c = 1

igual = True if a == b and a == c else False"""

compara = lambda x,y,z : bool( x == y ) and bool( x == z )

"""A = 2
B = 1
C = 2
D = 2
IGUAL = True if A == B and A == C and A == D else False
"""

iguales4 = lambda x,y,z,q : bool( x == y ) and bool( x == z ) and bool( x == q )

"""
x = 4
y = 5

igual = ( str(y) + "," + str(x) ) if x >= y  else ( str(x) + "," + str(y) )
"""

igual = lambda x, y : ( str(y) + "," + str(x) ) if x >= y  \
                                                else ( str(x) + "," + str(y) )

"""from math import gcd
hola = (14*6)/gcd(14,6)"""
from math import gcd
mcm = lambda x,y : int(( x * y ) / gcd( x, y ))

""""Quitar espacios"
entrada = "Esto es una prueba"
salida = entrada.replace(" ","")"""

quitaesp = lambda x : x.replace(" ", "")

"Comparando cadenas"
salida = lambda x, y : x.lower() == y.lower()

"""
acentos = x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")
salida = x.translate(acentos)
"""

noacento = lambda x : "" if x == "" else x.translate(x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU"))

"Palindromo"
palindrome = lambda x : \
    x.translate(x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")).replace(" ", "").lower() \
          == x.translate(x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")).replace(" ", "").lower()[::-1]

"Repetir Cadena"
repite = lambda x, y : x * y if y >= 0 else x

"Comprobar vocal"
vocales = ["a","e","i","o","u"]
esvocal = lambda x : x.translate(x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")).replace(" ","").lower() in\
    vocales if x != "" else "Cadena vacia"

"""Calculadora
x = primer operando
y = segundo operando
z = operador

"""

calcula = lambda x,y,z: x + y if z == '+' else \
    x - y if z == '-' else \
        x * y if z == '*' else \
            int(x / y) if z == '/' else "Tu que eres muy listo?"

"""
Distancia euclidiana
"""
from math import sqrt
eucli = lambda x1, y1, x2, y2 : sqrt( ( ( x1 - x2 ) ** 2 ) + ( ( y1 - y2) ** 2 ) )

"""Calcular segundos"""

segundos = lambda x,y,z: str( ( x * 24 * 60 * 60 ) + ( y * 60 * 60 ) + z ) + " " + "Segundos"

"""distancia(1,30,0,30) 60"""

distancia = lambda hora1, minuto1, hora2, minuto2: \
    ( ( hora1 * 60 ) + minuto1 ) - ( ( hora2 * 60 ) + minuto2 ) \
         if ( hora1 >= 0 \
              and minuto1 >= 0 \
              and hora2 >= 0 \
              and minuto2 >= 0 ) \
         else 'Negativos no'



