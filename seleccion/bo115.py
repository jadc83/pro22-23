"""
115. Escribir un programa que lea un archivo de texto (cuyo nombre lo solicitará por teclado
al usuario) y muestre su contenido por pantalla.

"""

archivo = open("bo115.txt", "r")
texto = archivo.read()
archivo.close()
print(texto)