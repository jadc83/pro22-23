"""
La suma lenta es un algoritmo para sumar dos numeros
para el que solo necesitamos saber cuales son el 
anterior y el siguiente de un numero dado, el algoritmo
se basa en la siguiente recurrencia:


                b si                          a = 0
suma_lenta(a,b)
                suma_lenta(ant(a), sig(b)) si a > 0
                
                
pre >>> a >= 0
suma_lenta(a: float / int, b: float / int) >>> float / int
post >>> suma_lenta(a,b) = ( a - 1 ) + ( b + 1 )



"""

ant = lambda n: n - 1
sig = lambda n: n + 1

suma_lenta = lambda a,b : b if a <= 0 else \
    suma_lenta(ant(a), sig(b))
