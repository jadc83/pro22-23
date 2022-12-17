"""
11. Escribir un programa que calcule el mínimo común múltiplo (mcm) de dos números
enteros, de dos formas diferentes:
a) Mediante la función lcm del módulo math.
b) Aprovechando la siguiente propiedad:
a · b = 𝑚𝑐𝑑 (a, b) · 𝑚𝑐𝑚(a, b)

"""
from math import gcd

a = 8
b = 2

mcm = (a * b) / gcd(a, b)