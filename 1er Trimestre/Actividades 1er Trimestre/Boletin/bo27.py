"""
27. Escribir un programa que solicite al usuario un número comprendido entre 1 y 7,
correspondiente a un día de la semana. Se debe mostrar el nombre del día de la semana
al que corresponde. Por ejemplo, el número 1 corresponde a «lunes» y el 6 a «sábado»
"""

semana = {1: "Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves", 5: "Viernes", 6: "Sabado", 7: "Domingo"}
numero = int(input("Introduce numero: \n"))
print(semana[numero])