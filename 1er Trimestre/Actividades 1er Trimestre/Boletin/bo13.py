"""
13. Un biólogo está realizando un estudio de distintas especies de invertebrados y necesita
un programa que le ayude a contabilizar el número de patas que tienen en total todos
los animales capturados durante una jornada de trabajo. Para ello, te ha solicitado que
escribas un programa al que hay que proporcionar:
• El número de hormigas capturadas (6 patas).
• El número de arañas capturadas (8 patas).
• El número de cochinillas capturadas (14 patas).
El programa deberá mostrar el número total de patas.

"""

hormigas = int(input("Cuantas hormigas?\n"))
arañas = int(input("Cuantas arañas?\n"))
cochi = int(input("Cuantas cochinillas?\n"))

total = ( hormigas * 6 ) + ( arañas * 8 ) + ( cochi * 14 )
print(total)
