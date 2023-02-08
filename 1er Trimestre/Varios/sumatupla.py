'''
Sumatupla iterativa
'''
'''
Sumatupla
'''

sumat = lambda t , acu: acu if t == () else \
                                           sumat(t[1:], acu + t[0])
sumatupla = lambda t: sumat(t,0)

'''
Media de sumatupla
'''
media = lambda t , acu, cont : acu / cont if t == () else \
                                           media(t[1:], acu + t[0], cont + 1)
mediatupla = lambda t: media(t,0,0)

"""dasdadsad"""