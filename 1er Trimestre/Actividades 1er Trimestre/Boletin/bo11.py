"""
11. Escribe un programa que solicite al usuario que introduzca una cantidad de segundos.
El programa deberá mostrar cuántas horas, minutos y segundos hay en el número de
segundos introducidos por el usuario.

"""

segundos = int(input("Introduce una cantidad de segundos:\n"))

horas = segundos // 60 // 60
hsec = horas * 60 * 60
nsecs = segundos - hsec
minutos = nsecs // 60
msecs = minutos * 60
final = (nsecs) - msecs

print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {final} segundos.")