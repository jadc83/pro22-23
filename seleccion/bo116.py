"""
116. Pedir por teclado el nombre, la edad (un entero) y la estatura en metros (un real) de
un deportista. Si algún dato tiene un formato incorrecto, deberá indicarse. En caso
contrario, se deberá mostrar todos los datos en pantalla.

"""

nombre = input("Introduce nombre:\n")
try:
    edad = int(input("Introduce edad:\n"))
    estatura = float(input("Introduce altura en metros:\n"))
except ValueError:
    print("Formato de los datos incorrecto.")
    
print(f"Nombre: {nombre}\nEdad: {edad}\nEstatura: {estatura}")