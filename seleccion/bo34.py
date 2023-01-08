"""
34. Escribir un programa para calcular datos estadísticos de las edades de los alumnos de
un centro educativo. Se introducirán datos hasta que uno de ellos sea negativo, y se
mostrará: la suma de todas las edades introducidas, la media, el número de alumnos y
cuántos son mayores de edad.
"""

lista = []
edad = 0
while edad >= 0:
    edad = int(input("Introduce edad:\n"))
    if edad >= 0:
        lista.append(edad)
mayores = len([x for x in lista if x > 17])        
print(f"La suma es {sum(lista)}, la media es {round(sum(lista) / len(lista), 2)}, \
        para {len(lista)} alumnos, de los cuales {mayores} son mayores de edad")
