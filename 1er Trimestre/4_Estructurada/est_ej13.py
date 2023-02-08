"""
13. Los datos de los empleados de una empresa se almacenan en una lista de tuplas, donde
cada tupla representa a un empleado de la siguiente forma:

(nombre, apellidos, salario)
En el programa, los cuatro empleados que tiene la empresa se almacenan en la siguiente
lista:
empleados = [('María', 'González', 1800.23),
('Javier', 'Ruiz', 1630.50),
('Jesús', 'Pérez', 2100.42),
('Rosa', 'Muñoz', 2240.78)]
Se pide escribir un programa que modifique la lista de empleados incrementando en un
10 % el salario de cada empleado y muestre por pantalla el salario total de los empleados
de la empresa
"""
i = 0 # Acumulador para calcular total
N = 0 # Indice incrementable
lista = []
empleados =[('María', 'González', 1800.23),
            ('Javier', 'Ruiz', 1630.50),
            ('Jesús', 'Pérez', 2100.42),
            ('Rosa', 'Muñoz', 2240.78)]

######################################
copiaemple = [list(x) for x in empleados]
######################################

while N <= len(copiaemple) - 1:
    copiaemple[N][2] = round(copiaemple[N][2] * 1.1,2)
    i += copiaemple[N][2]
    N += 1

###################################
emple = [tuple(x) for x in copiaemple]
###################################

#print(emple)
print("Salario total:" )
print(i, "€")
