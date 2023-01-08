"""
4. Escribe un programa que solicite las notas del primer, segundo y tercer trimestre (notas
enteras que se solicitarán al usuario). El programa debe mostrar la nota media del curso
como se utiliza en el boletín de calificaciones (sólo la parte entera) y como se usa en el
expediente académico (con decimales).
"""
import math
nt1 = float(input("Introduce nota del primer trimestre:\n"))
nt2 = float(input("Introduce nota del segundo trimestre:\n"))
nt3 = float(input("Introduce nota del tercer trimestre:\n"))

nota1 = math.trunc((nt1 + nt2 + nt3) / 3)
nota2 = (round(((nt1 + nt2 + nt3) / 3), 1))

print(f"La calificacion para el boletin es {nota1} y la calificacion para el expediente es {nota2}") 