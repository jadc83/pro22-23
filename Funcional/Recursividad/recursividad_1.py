"""Ejercicios Recursividad

1)  Dada la funcion matematica:

     0 si n = 0
f(n)
     1 + 2 * f(n-1) si n > 0
     
     
funcion(3) == 7
"""

funcion = lambda n : 0 if n == 0 else \
                1 + 2 * funcion(n - 1) if n > 0 \
                    else "hola"      
