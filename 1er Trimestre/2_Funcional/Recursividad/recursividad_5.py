"""
La funcion suma_digitos calcula la suma de los digitos
de un numero entero:

suma_digitos(423) = 4 + 2 + 3 = 9
suma_digitos(7) = 7

Se pide:

a) Escribir su especificacion.
b) Implementar una funcion recursiva que satisfaga dicha
   especificacion
   
   pre >>> n debe ser int
   suma_digitos(n: int) >>> int
   suma_digitos(n) = int
   
   
"""


suma_digitos = lambda n : n if abs(n) <= 0 else \
    abs(n) % 10 + suma_digitos(n // 10 )
