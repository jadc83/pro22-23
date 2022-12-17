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
