"""
2. Un frutero necesita calcular los beneficios anuales que obtiene de la venta de manzanas
y peras. Por este motivo, es necesario diseñar un programa que solicite las ventas (en
kilos) de cada semestre para cada fruta. El programa mostrará el importe total sabiendo
que el precio del kilo de manzanas está fijado en 2.35 € y el kilo de peras en 1.95 €
"""

manzanas = float(input("Introduce la cantidad de manzanas:\n")) * 2.35
peras = float(input("Introduce la cantidad de peras:\n")) * 1.95

total = manzanas + peras
print(f"Se han vendidos manzanas y peras por la cantidad de {total}€ este trimestre.")
