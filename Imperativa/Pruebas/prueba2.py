"""
nombre = input("Introduce Nombre:")
apellidos = input("Introduce Apellidos:") 
direccion = input("Introduce Direccion: ")
importe = input("Introduce Importe Total: ")

archivo = open("factura.txt", "w+")
archivo.seek(0)
archivo.write(
    "---------------------------------------------------------\n" +
    "Nombre: " + nombre + "\n" +
    "Apellidos: " + apellidos + "\n" +
    "Direccion: " + direccion + "\n" +
    "Importe: " + importe + "€\n" +
    "---------------------------------------------------------")
archivo.close()
"""

for rama in range(1,30,4):
    print(('*'*rama).center(30))

for palo in range(1):
    print(('|||').center(30))
print(('\_______/').center(30))
print(' '+30*'-')
