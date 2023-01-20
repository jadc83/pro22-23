"""
71. Escribir una función a la que se le pase como argumentos una cantidad de días, horas y
minutos. La función calculará y devolverá el número de segundos que existen en los
datos de entrada.

"""

def segundos(dia, hora, minuto):
    segundo = 0
    
    minutos = hora * 60
    horas = hora * 60 * 60
    dias = dia * 24 * 60 * 60
    
    segundo = minutos + horas + dias
    print(segundo)