'''
La funcion par determina si un numero entero (positivo
o negativo) es par:

par(0) = True
par(1) = False
Par(-27) = False

a) Escribir su especificacion
b) Implementar una funcion recursiva que satisfaga
   dicha especificacion.
c) Como se podria implementar una funcion impar a partir
   de la funcion par?
'''
'''
a) pre: True
    par(n: int) >>> bool
   post: par(n) determina si un numero entero es par o no
'''
'''
b)
'''
par = lambda n: True if n == 0 else \
    not par(abs(n) - 1)
'''
c)
'''
impar = lambda n: True if n == 0 else \
    par(abs(n) - 1)

impar2 = lambda n: not par(n)
