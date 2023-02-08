"""
6. Escribe un programa que pida el año actual y el de nacimiento del usuario. Debe calcular
su edad, suponiendo que en el año en curso el usuario ya ha cumplido años.
"""

edad = int(input("¿En que año naciste?\n"))

fecha = int(input("¿En que año estamos?\n"))

print(f"Tu edad es de { fecha - edad } años")