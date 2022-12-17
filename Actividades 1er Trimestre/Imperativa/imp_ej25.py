"""
25. Escribir un programa que lea dos listas de números enteros no ordenados de sendos
archivos con un número por línea, los reúna en una lista única y los guarde en orden
creciente en un tercer archivo, de nuevo uno por línea.
"""

archivo1 = open("lista1.txt", "r")                #Apertura del primer archivo
lista1 = archivo1.readlines()                     #Copia de la primera lista
archivo1.close()                                  #Cierre del primer archivo

archivo2 = open("lista2.txt", "r")                #Apertura del segundo archivo
lista2 = archivo2.readlines()                     #Copia de la segunda lista
archivo2.close()                                  #Cierre del segundo archivo

concatenadas = lista1 + lista2                    #Concatenacion de cadenas
entero = sorted([int(x) for x in concatenadas])   #Se hace un cambio de tipo para ordenar correctamente
cadena = [str(x) for x in entero]                 #Se vuelve a convertir a cadena para añadir salto de linea
consalto = [ x + "\n" for x in cadena]            #Añadir salto de linea
consalto[-1] = consalto[-1].strip()               #Eliminar el ultimo salto de linea.

archivo3 = open("lista34.txt", "w+")              #Apertura del tercer archivo
archivo3.writelines(consalto)                     #Escritura del resultado en el tercer archivo
archivo3.close()                                  #Cierre del tercer archivo.
