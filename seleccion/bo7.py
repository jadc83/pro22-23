"""
7. Escribe un programa que tome como entrada un número entero e indique qué cantidad
hay que sumarle para que el resultado sea múltiplo de 7. Un ejemplo:
• A 2 hay que sumarle 5 para que el resultado (2 + 5 = 7) sea múltiplo de
7.
• A 13 hay que sumarle 1 para que el resultado (13 + 1 = 14) sea múltiplo de 7.
Si proporcionas el número 2 o el 13, la salida del programa debe ser 5 ó 1, respectivamente.
Indicación: Usar el operador módulo.
"""
numero = int(input("Mete numero:\n"))
cifra = numero
contador = 0
while cifra % 7 != 0:
    cifra += 1
    contador += 1
print(f"{numero} + {contador} es multiplo de 7 ({numero + contador})")