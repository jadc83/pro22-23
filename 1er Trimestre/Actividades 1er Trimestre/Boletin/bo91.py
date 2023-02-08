"""
91. Crear una matriz bidimensional de tamaño 5 × 5 mediante una lista de listas y rellenarla
de la siguiente forma: el elemento de la posición [𝑛][𝑚] debe contener el valor 10·𝑛+𝑚.
Después se debe mostrar su contenido.

"""


matriz = [ 
           [],
           [],
           [],
           [],
           [],          
         ]

for n in range(0,5):
    for m in range(0,5):
        matriz[n].append(10 * n + m)
    
    print(matriz[n])