'''

dsadadasd
'''
quita = lambda e, t, c: () if t == () else \
    0 if e in t else 1
'''
quitatupla recursivo
'''

aux = lambda a, b : (b,) if a != b else ()

quita = lambda e, t: () if t == () else \
    aux(e, t[0]) + quita(e, t[1:] )


'''
Quitatupla iterativo
'''


quitaiter = lambda x, y, z : z if y == () else \
    quitaiter( x, y[1:], z + ( y[0],) ) if y[0] != x else \
        quitaiter( x, y[1:], z )

quitar = lambda x, y : quitaiter( x, y, () )