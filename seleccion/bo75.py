"""
75. Crear tres listas de cinco elementos: la primera con enteros, la segunda con reales y la
tercera con booleanos.

"""
enteros = []
while len(enteros) != 5:
    try:
        ent = int(input("Mete entero perro:\n"))
        enteros.append(ent)
    except ValueError:
        print("No es el tipo correcto")
reales = []
while len(reales) != 5:
    try:
        ent = float(input("Mete float perro:\n"))
        reales.append(ent)
    except ValueError:
        print("No es el tipo correcto")
buleanoh = []
while len(buleanoh) != 5:
    try:
        ent = int(input("Mete 0 o 1 perro:\n"))
        if ent == 0:
            buleanoh.append(False)
        if ent == 1:
            buleanoh.append(True)
    except ValueError:
        print("No es el tipo correcto")