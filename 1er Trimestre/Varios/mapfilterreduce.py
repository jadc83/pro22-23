"elevar los divisores primos de un numero desde 1 hasta n"
"""divisores = lambda n: filter(lambda e: n % e == 0, range(1, n + 1)) #De aqui salen los divisores de n
primos = lambda n: False if ( True in map(lambda e: n % e == 0, range( 2, n ) ) ) else True #
sonprimos = lambda n: filter(lambda n: primos(n) , range(1, n + 1 ))
cuadrado = lambda n: map(lambda e: e**2, sonprimos(n))
final = lambda a: reduce(lambda x,y: x+y, cuadrado(a))"""

from functools import reduce
divisores = lambda n: tuple(filter(lambda d: n % d == 0,  range(1, n ) ) ) #Esta funcion devolvera los divisores contenidos entre 1 y n (n se vende por separado)
primos = lambda p: len(divisores(p) ) == 2 #Esta funcion sera usada por sonprimos()
sonprimos = lambda s: filter( primos, range( 1, s ) ) #Esta funcion devolvera los divisores primos de n
eleva = lambda p: map(lambda e: e ** 2, sonprimos( p ) ) #Esta funcion los elevara al cuadrado
suma_primos = lambda p: reduce(lambda x, y: x + y, eleva( p ) ) #Esta funcion sumara el contenido de la tupla resultante