""""
26. Escribir un programa que lea un archivo de texto llamado carta.txt. Tenemos que
contar los caracteres, las líneas y las palabras. Para simplificar, supondremos que cada
palabra está separada de otra por un único espacio en blanco o por un salto de línea

"""

from functools import reduce
suma = lambda a, b: a + b

########################################################################

archivo = open("carta.txt")
carta = archivo.readlines()
archivo.close()

#########################################################################

lineas = len(carta) ### Numero de lineas
junta =  reduce(suma, carta) #Concateno la lista de cadenas en una sola
caracteres = len(junta) ### Numero de caracteres

###############################SALIDA####################################

print(caracteres)
print(lineas)
print(len(junta.split())) ### Numero de palabras