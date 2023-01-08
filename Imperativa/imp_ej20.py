"""
20. Crear un archivo de texto con una colección de números reales, uno por línea. A
continuación, escribir un programa que:
a. Abra el archivo para lectura.
b. Lea todas sus líneas.
c. Muestre finalmente la suma de todos ellos.

"""
from functools import reduce
suma = lambda a, b: a + b

fichero = open("numeros_reales2.txt", "r") #Se abre el fichero en modo lectura
copiafichero = fichero.readlines() #Se vuelca el contenido del fichero en forma de lista
fichero.close() #Se cierra el fichero
quitasalto = ["".join(x.strip()) for x in copiafichero] #Se eliminan los caracteres de salto de linea
palmap = reduce(suma, quitasalto).split() #Una vez limpias las cadenas, se separan los valores y se concatena todo en un elemento
toint = tuple(map(int, palmap)) #Se hace la conversion a INT de todos los elementos
final = reduce(suma, toint) #Se suman todos sus elementos, #Fin
print(final)
