from functools import reduce
suma = lambda a, b: a + b

numeros = [ input('Mete numero aqui: ') for x in range(1,6) ]
entero = [ float(x) for x in numeros ]
longi = len(entero)
numero = reduce(suma, entero)
print(numero / longi)