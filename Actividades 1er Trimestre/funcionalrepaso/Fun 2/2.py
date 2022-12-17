potencia = lambda a, b: a ** b if b != 0 else 1


potencia_rec = lambda a,b: 1 if b <= 0 else \
    a * potencia_rec(a , b - 1)