"""dropwhile"""

dejar_mientras = lambda funcion, tupla: () if tupla == () else \
    dejar_mientras(funcion, tupla[1:]) if funcion(tupla[0]) else \
        tupla
        
        
dejar_mientra = lambda f, t: () if t == () else \
    t if not f(t[0]) else \
        dejar_mientra(f, t[1:])