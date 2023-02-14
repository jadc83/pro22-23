def racional(a, b):
    numerador, denominador = a, b
    return [a, b]

def numer(lista):
    return lista[0]

def denom(lista):
    return lista[1]

def suma(a, b):
    num_a, den_a = numer(a), denom(a)
    num_b, den_b = numer(b), denom(b)
    return [ ( num_a * den_b ) + ( num_a * den_a ), den_a * den_b ]

def multiplicar(a, b):
    return racional(numer(a) * numer(b), denom(a) * denom(b))
    
def iguales(a, b):
    return numer(a) * denom(b) == numer(b) * denom(a)

def imprimir(a):
    print(numer(a), '/', denom(a), sep='')

