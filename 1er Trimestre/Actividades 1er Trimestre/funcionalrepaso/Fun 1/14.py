"""
14. Usando el método maketrans1 definido sobre las cadenas, escribir un programa que
sustituya en una cadena las vocales acentuadas por sus correspondientes sin acentuar.
Por ejemplo, si la entrada es la cadena "¡Ramón! ¡Cuánto tiempo! ¿Cómo estás?", la
salida deberá ser "¡Ramon! ¡Cuanto tiempo! ¿Como estas?".


"""

cadena = "Ramón! Cuánto tiempo! ¿Cómo estás?"

meiktran = cadena.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")

final = cadena.translate(meiktran)