"""
1. Escribir un programa que nos indique si podemos salir a la calle. Existen aspectos que
influirán en esta decisión: si está lloviendo y si hemos terminado nuestras tareas. Solo
podremos salir a la calle si no está lloviendo y hemos finalizado nuestras tareas. Existe
una opción en la que, indistintamente de lo anterior, podremos salir a la calle: el hecho
de que tengamos que ir a la biblioteca (para realizar algún trabajo, entregar un libro, etc.).
Preguntar al usuario si llueve, si ha finalizado las tareas y si necesita ir a la biblioteca. El
programa deberá mostrar (mediante un mensaje Sí o No) si es posible que se le otorgue
permiso para ir a la calle.

"""
biblio = input("Tienes que ir a la biblioteca?\n").lower()
if biblio == "no":
    lluvia = input("Llueve?\n").lower()
    if lluvia == "no":
        tareas = input("Te quedan tareas por hacer?\n").lower()
        if tareas == "si":
            print("No puedes salir")
        else:
            print("Puedes salir")
    else:
        print("No puedes salir")
elif biblio == "si":
    print("Si")