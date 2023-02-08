"""
46. Dadas 6 notas, escribir la cantidad de alumnos aprobados, condicionados (nota igual a
4) y suspensos.
"""

calificaciones = []
aprobados = 0
suspensos = 0
condicionados = 0

for x in range(1,7):
    calificaciones.append(int(input("Mete nota:\n")))
    
for x in calificaciones:
    if x == 4:
        condicionados += 1
    elif x < 4:
        suspensos += 1
    elif x > 4:
        aprobados += 1
        
if suspensos != 0:
    print(f"Hay {suspensos} suspensos, {condicionados} condicionados y {aprobados} aprobados")