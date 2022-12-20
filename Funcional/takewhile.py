
"""tomar_mientras = lambda c, sec, i: i if sec == () else \
    tomar_mientras(c, sec[1:], i + (sec[0],)) if sec[0] < c else \
        i
"""
        
tomar_mientra = lambda funcion, tupla, acumulador: acumulador if tupla == () else \
    tomar_mientra(funcion, tupla[1:], acumulador + (tupla[0],)) if funcion(tupla[0]) else \
        acumulador
        
tomar_mientras = lambda funcion, tupla: tomar_mientra(funcion, tupla, ())