

"""
Volumen
from math import pi
v = ( 4 / 3 ) * ( pi * ( r ** 3 ) )
"""
from math import pi
volumen = lambda r: 'r no puede ser 0' if r <= 0 else round(( 4 / 3 ) * ( pi * ( r ** 3 )), 3)
