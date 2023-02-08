"""
La funcion potencia tiene la siguiente especificacion:

    pre >>> b >= 0
    potencia(a: int, b: int) >>> int
    potencia(a,b) = a ** b
    
    

    a * ( potencia(a, b - 1))
    
    
potencia = lambda a,b : a ** b if b >= 0 else 0

"""


recpow = lambda a,b: 1 if b <= 0 else a * recpow(a, ( b - 1 ) )
