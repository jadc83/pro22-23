"""
7. Dado el siguiente código:
1 n = int(input('¿Hasta dónde llego?: '))
2 i = 0
3 while i < n:
4 print('Aquí la i vale', i)
5 i += 2

se pide:
a) Contar cuántas sentencias hay. #### 5 sentencias
b) Por cada una de ellas, indicar si son simples o compuestas. 

    n = int(input('¿Hasta dónde llego?: ')) ### Simple      Asignacion
    i = 0                                   ### Simple      Asignacion
    while                                   ### Compuesta   Condicional
     print('Aquí la i vale', i)             ### Simple      print
     i += 2                                 ### Simple      Asignacion

c) Por cada sentencia compuesta, indicar de qué tipo de estructura se trata.

d) Deducir cuántas veces se ejecuta la sentencia de la línea 4 en función del valor de
la variable 
        n. #### n - 1 veces

e) ¿Es posible provocar un bucle infinito al ejecutar ese programa?

"""

n = int(input('¿Hasta dónde llego?: '))
i = 0
while i < n:
    print('Aquí la i vale', i)
    i -= 2


