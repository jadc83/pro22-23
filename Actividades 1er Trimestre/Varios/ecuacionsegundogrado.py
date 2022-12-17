from math import sqrt
a = 2
b = 32
c = 42
arriba1 = (-b - (sqrt(pow( b, 2 ) - 4 * a * c ))) 
arriba2 = (-b + (sqrt(pow( b, 2 ) - 4 * a * c )))
abajo = ( 2 * a )

s1 = arriba1 / abajo if arriba1 >= 0 else 'Error'
s2 = arriba2 / abajo if arriba2 >= 0 else 'Error'

