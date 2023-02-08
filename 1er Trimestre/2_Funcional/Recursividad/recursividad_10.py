'''
contar
'''

'''Recursivo'''
aux = lambda a, b: 1 if a == b else 0

cuantos = lambda e, t: 0 if t == () else \
aux(e, t[0]) + cuantos(e, t[1:])
    
'''Iterativo'''
cuentaiter = lambda e, t, c: c if t == () else \
    cuentaiter(e, t[1:], c + 1) if e in (t[0],) else \
    cuentaiter(e, t[1:], c)
