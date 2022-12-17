'''
La funcion elem tiene la siguiente especificacion:

pre: True
        elem(e, t: tuple) >>> bool
        
     Post: elem(e,t) = True si e esta en t
                       False en caso contrario

Escribe una funcion recursiva que satisfaga dicha especificacion
'''

elem = lambda e, t : False if t == () else \
    True if e == t[0] else \
        elem(e, t[1:])
