"""Inversa"""
inversa = lambda tupla: () if tupla == () else \
    inversa( tupla[1:] ) + (tupla[0],)