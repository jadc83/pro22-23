"""dASDQWFwdfwsd"""
import os
PULSA = '' ### Esto ejerce de interruptor para el menu principal
lista = []
def borrar():
    return os.system("cls")
while PULSA == '':
    print("Menu")
    print("1. Añadir un elemento a la lista.")
    print("2. Cambiar el valor de un elemento de la lista.")
    print("3. Eliminar un elemento de la lista.")
    print("4. Eliminar todos los elementos de la lista.")
    print("5. Mostrar los elementos de la lista.")
    print("0. Salir del programa.")
    print()
    option = input("Seleccione opcion:\n")

#############################################################
    if option == "1":
        borrar()
        dato = input("Que quiere añadir?\n")
        lista = lista + [dato,]
        input("Presione ENTER para volver")
        borrar()

#############################################################
    elif option == "2":
        borrar()
        option = input("Que valor quiere cambiar?\n")
        nuevo = input("Cual es el nuevo valor?\n")
        print("Aqui cambio el valor")
        input("Presione ENTER para volver")
        borrar()

#############################################################

    elif option == "3":
        borrar()
        option = input("Cual es el elemento a eliminar?\n")
        lista.remove(option)
        print("Presione ENTER para volver")
        borrar()

#############################################################

    elif option == "4":
        borrar()
        option = input("Se va a vaciar la lista\n")
        lista = []
        input("Lista vacia, presiona ENTER para volver")
        borrar()

#############################################################

    elif option == "5":
        borrar()
        print(lista)
        input("Pulse ENTER para volver")
        borrar()
    elif option == "0":
        break
