"""
12. Escribir un programa que gestione datos almacenados en una lista, de forma que muestre
un menú con las siguientes opciones:
1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.
El programa deberá pedir la información necesaria para cada opción elegida por el
usuario
"""
import os

def borrar():
    """Borra la pantalla"""
    return os.system("cls")

borrar()
lista = []
opt = ""
while opt == "" :
    print("1. Añadir un elemento a la lista.")
    print("2. Cambiar el valor de un elemento de la lista.")
    print("3. Eliminar un elemento de la lista.")
    print("4. Eliminar todos los elementos de la lista.")
    print("5. Mostrar los elementos de la lista.")
    print("Pulse 0 para salir.")
    print()
    opcion = input("Selecciona una opcion: ")
    borrar()
    if opcion == "1":
        borrar()
        e = input("Inserte el elemento a añadir:\n")
        borrar()
        input(f"El elemento {e} se ha añadido a la lista\n\nPulse cualquier tecla para volver")
        lista.append(e)
        borrar()
        
    elif opcion == "2":
        borrar()
        acambiar = int(input("Cual es el indice del elemento a cambiar?\n"))
        borrar()
        nuevoe = input("Cual es el nuevo elemento?\n")
        lista[acambiar] = nuevoe
        input("Elemento cambiado\n\nPresione cualquier tecla para continuar.")
        borrar()

    elif opcion == "3":
        borrar()
        print("Eliminar un elemento de la lista")
        aborrar = int(input("Cual es el indice del elemento a eliminar?\n"))
        lista.pop(aborrar)
        input("Elemento eliminado\n\nPulse cualquier tecla para volver")
        borrar()

    elif opcion == "4":
        borrar()

        input(f"Se eliminaran todos los elementos de la lista\n\nPulse ENTER para confirmar.")
        lista = []
        
        borrar()
    elif opcion == "5":
        borrar()
        print("A continuacion se muestran los elementos de la lista (derecha) y el indice asignado.(Izquierda)")

        print()
        for count, i in enumerate(lista, 0):
            print(count, i)
        print()

        input("Presione cualquier tecla para volver.")
        borrar()
    elif opcion == "0":
        break
