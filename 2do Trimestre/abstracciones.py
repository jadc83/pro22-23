import sys

def racional(a, b):
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
    
def combo(a,b):
    maestra = "jalapeño"
    def ninja(indice):
        if indice == 0:
            return a
        elif indice == 1:
                return b
    return ninja

def select (p, i):
    return p(i)

def prueba():
    return len(sys.argv)