"""
12. Solicita al usuario tres distancias:
• La primera, medida en milímetros.
• La segunda, medida en centímetros.
• La última, medida en metros.
Escribe un programa que muestre la suma (en centímetros) de las tres longitudes
introducidas.
"""

mm = int(input("Introduce milimetros:\n"))
cm = int(input("Introduce centimetros:\n"))
m =  int(input("Introduce metros:\n"))

total = ( mm / 10) + cm + ( m * 100)
print(total)