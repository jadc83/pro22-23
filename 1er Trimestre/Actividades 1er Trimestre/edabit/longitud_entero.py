def number_length(num):
    num = str(num)
    contador = 0
    while num != '':
        num = num[1:]
        contador += 1
    return contador
    