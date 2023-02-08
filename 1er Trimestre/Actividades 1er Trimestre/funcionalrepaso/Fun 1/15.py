"""
15. Escribir un programa que diga si una cadena es un palíndromo.
Un palíndromo es una cadena que se lee igual de izquierda a derecha que al revés. Por
ejemplo: «Dábale arroz a la zorra el abad».
Deben ignorarse las tildes, las mayúsculas y los espacios en blanco. Para ello, hacer uso
de las soluciones encontradas en los ejercicios anteriores

"""

cadena = "Dábale arroz a la zorra el abad"
traduccion = cadena.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")
cadenita = cadena.translate(traduccion).replace(" ","").lower()

invertir = lambda n: n if n == "" else invertir(n[1:]) + str(n[0])

palindromero = cadenita == invertir(cadenita)