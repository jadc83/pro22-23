from functools import reduce
suma = lambda a, b: a + b

numeros = [ float(input('Mete numero aqui: ')) for x in range(1,6) ]
longi = len(numeros)
numero = reduce(suma, numeros)
print(numero / longi)