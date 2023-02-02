"""
118. Un libro de firmas es útil para recoger los nombres de todas las personas que han pasado
por un determinado lugar. Escribir un programa que permita mostrar el libro de firmas
e insertar un nuevo nombre (comprobando que no se encuentre repetido). El archivo se
deberá llamar firmas.txt.
"""

contenido = []
while True:
    print("[LIBRO ELECTRONICO DE FIRMAS]")
    print("1) Deja tu firma")
    print("2) Ver firmas.")
    print("3) Salir")
    opcion = input("Selecciona la opcion deseada:\n")
    if opcion == "1":
        archivo = open("firmas.txt", "r")
        contenido = archivo.readlines()
        archivo.close()
        contenido = [x.strip() for x in contenido]
        nombre = input("Introduce tu firma:\n")
        if nombre not in contenido:
            archivo = open("firmas.txt", "a")
            archivo.write("\n")
            archivo.write(nombre)
            archivo.close()
        else:
            print("La firma ya esta presente.")
            input()
    elif opcion == "2":
            archivo = open("firmas.txt", "r")
            contenido = archivo.readlines()
            archivo.close()
            for x in contenido:
                print(x, end="")
            input()
    elif opcion == "3":
        break
    