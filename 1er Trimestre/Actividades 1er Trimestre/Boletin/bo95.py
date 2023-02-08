"""
95. En un juego de rol, el mapa puede implementarse como una matriz donde las filas y las
columnas representan lugares (lugar 0, lugar 1, lugar 2, etc.) que estarán conectados. Si
desde el lugar 𝑥 podemos ir hacia el lugar 𝑦, entonces la matriz en la posición [𝑥][𝑦]
valdrá True; en caso contrario, valdrá False.
Escribe una función que, dados dos lugares y una matriz que representa el mapa, indique
si es posible viajar desde el primer lugar al segundo directamente o pasando por
lugares intermedios
"""


mapa = {1:1, 2:1, 3:0, 4:0,
        5:0, 6:1, 7:1, 8:0,
        9:0, 10:0, 11:1, 12:1,
        13:0, 14:0,15:0, 16:0}

camino = []
for x,y in mapa.items():
        if y == 1:
                camino.append(x)
                

print(sorted(camino))