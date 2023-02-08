
'''
La funcion par_positivo determina si un numero entero
positivo es par:

par_positivo(0) = True
par_positivo(1) = False
par_positivo(27) = False
par_positivo(82) = True
'''


par_positivo = lambda n: True if n <= 0 else \
        True if n % 2 == 0 else False

iterpar_positivo = lambda n: False if n <= 0 else \
    not iterpar_positivo(n - 1)

iterimpar_positivo = lambda n: False if n == 0 else \
    not iterimpar_positivo(n - 1)
    

