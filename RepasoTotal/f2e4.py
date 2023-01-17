"""
4. La suma lenta es un algoritmo para sumar dos números para el que sólo necesitamos
saber cuáles son el anterior y el siguiente de un número dado. El algoritmo se basa en
la siguiente recurrencia:
su𝑚a_lenta(a, b) =
(
b si a = 0
su𝑚a_lenta(ant(a), sig(b) si a > 0
Suponiendo que tenemos las siguientes funciones ant y sig:
ant = lambda n: n - 1
sig = lambda n: n + 1
Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.

"""

ant = lambda n: n - 1
sig = lambda n: n + 1

suma_lenta = lambda a, b: b if a <= 0 else \
    ant(a) + sig(b)
    
suma_lenta_rec = lambda a, b: b if a <= 0 else \
    suma_lenta_rec( (a - 1), (b + 1))

def suma_lenta_imp(num1, num2):
    return ant(num1) + sig(num2)

def suma_lenta_imp_rec(num1, num2):
    if num1 <= 0:
        return num2
    else:
        return suma_lenta_imp_rec(num1 - 1, num2 + 1)