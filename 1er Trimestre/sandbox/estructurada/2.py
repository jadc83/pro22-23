"""
Escribir una función escribir_fecha() que, aplicado a los datos 'D', 18, 9 y 60, dé lo siguiente:

Domingo, 18 de septiembre de 1960
"""

dname = {"D": "Domingo", "S": "Sábado", "V": "Viernes", "J": "Jueves", "X" : "Miércoles", "M": "Martes", "L": "Lunes"}
mname = {"1": "enero", 2: "febrero", 3: "marzo", 4: "abril", 5 : "mayo", 6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}

def escribir_fecha(letra, dia, mes, anyo):
    res = f"{dname[letra]}, {dia} de {mname[mes]} de 19{anyo}"
    return res