"""
50. Escribir un programa que incremente la hora de un reloj. Se pedirán por teclado la hora,
minutos y segundos, así como cuántos segundos se desea incrementar la hora introducida. El programa mostrará la nueva hora. Por ejempo, si las 13:59:51 se incrementan
en 10 segundos, resultan las 14:00:01.
"""

hora = input("Que hora es:\n")
segundo = input("Cuantos segundos")
hora_lista = hora.split(":")

horas = hora_lista[0]
minutos = hora_lista[1]
segundos = hora_lista[2]

if segundo > 59:
    minutos += 1
if segundo < 60:
    minutos += 1
