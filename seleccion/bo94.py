"""
94. Debes desarrollar una aplicación que ayude a gestionar las notas de un centro educativo.
Los alumnos se organizan en grupos compuestos por 5 personas. Leer las noas (números
enteros) del primer, segundo y tercer trimestres de un grupo. Debes mostrar al final la
nota media del grupo en cada trimestre y la media del alumno que se encuentra en una
posición dada (que el usuario introduce por teclado).
"""
alumno = int(input("Inserte alumno:\n"))
grupo1 = []
for x in range(0,5):
    notas = []
    for y in range(0,3):
            nota = int(input("Mete nota:\n"))
            notas.append(nota)
    grupo1.append(notas)
grupo1 = dict(list(enumerate(grupo1, 1)))

lista = []
lista1 = []
lista2 = []

for key in grupo1.keys():
    lista.append(grupo1[key][0])
    lista1.append(grupo1[key][1])
    lista2.append(grupo1[key][2])

print(f"La media del primer trimestre es {sum(lista) / len(lista)}")
print(f"La media del segundo trimestre es {sum(lista1) / len(lista1)}")
print(f"La media del tercer trimestre es {sum(lista2) / len(lista2)}")


    
