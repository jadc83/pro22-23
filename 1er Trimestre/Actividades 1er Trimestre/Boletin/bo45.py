"""
45. Pedir 5 calificaciones de alumnos y decir al final si hay algún suspenso
"""
calificaciones = []
aprobados = 0
suspensos = 0
condicionados = 0

for x in range(1,6):
    calificaciones.append(int(input("Mete nota:\n")))
    
for x in calificaciones:
    if x < 4:
        suspensos += 1
    else:
        aprobados += 1
        
if suspensos != 0:
    print(f"Hay {suspensos} suspensos.")