"""
La funcion voltea le da la vuelta a un numero entero:

voltea(423) = 324
voltea(7) = 7

Se pide:

a) Escribir su especificacion
b) Imprementar una funcion recursiva que satisfaga dicha
   especificacion
   
**Forma rapida no recursiva**
**voltea = lambda n : int(str(n)[::-1])

pre: -------------- true
voltea(n: int)  --- int
post: voltea(423) - 324
   
"""

digitos = lambda n: len(str(n)) - 1 if n <= 0 else len(str(n))
voltea = lambda n: n if digitos(n) <= 1 else \
    int(str(abs( n ) % 10 ) + str( voltea(abs( n ) // 10 )))
