"""
Escribir una función pasa_pasa() que manipule dos números enteros suprimiendo la última cifra del primero y añadiéndola al final del segundo.

Usando esa función, escribir la función invierte() que invierte un número (partiendo del propio número y de otro con valor inicial cero) a base de repetir la operación pasa_pasa() cuantas veces sea necesario.

Ambas funciones deben recibir como argumento una lista llamada numeros con los dos números sobre los que operan y deben cambiar dicha lista.

Además, la función invierte() debe mostrar cada paso del proceso, de la siguiente manera:

[12345, 0]
[1234, 5]
[123, 54]
[12, 543]
[1, 5432]
[0, 54321]
"""

def pasa_pasa(num1, num2):
    res = []
    res.append(num1 // 10)
    res.append( num2 + (num1 % 10) )
    return res

def invertir(numero1, veces):
    while veces != 0:
        res = pasa_pasa(numero1, 0)
        veces -= 1
        return res