"""
3. Convertir una cantidad de tiempo (en segundos, Z) en la correspondiente en horas, minutos y
segundos, con arreglo al siguiente formato:
3817 segundos = 1 horas, 3 minutos y 37 segundos

"""

Z = 3817
t = 60
horas = Z // t // t
minutos =  Z // t % t
segundos = Z % t

