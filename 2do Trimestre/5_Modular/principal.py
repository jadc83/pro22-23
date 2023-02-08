"""
a) Usar el módulo en otro llamado principal.py importándolo mediante:
from fibonacci import *
¿Cuáles son las funciones que se acaban importando de esta manera? ¿Por qué?
"""

from fibonacci import *
import sys

"""
b) El módulo debe probarse a sí mismo al ejecutarse desde la línea de órdenes del
sistema operativo (y sólo entonces):

i. Si se ejecuta sin argumentos en la línea de órdenes, deberá comprobar que
fib(8) y fib_iter(8) se calculan correctamente, mostrando un mensaje que
indique si el cálculo ha sido correcto o no. Por ejemplo:

$ python fibonacci.py
fib(8) vale 21 (correcto)
fib_iter(8) vale 37 (incorrecto)

ii. Si se ejecuta con un argumento en la línea de órdenes, deberá usarse como el
argumento de la función fib y mostrar por pantalla el resultado de la función.

Por ejemplo:
$ python fibonacci.py 7
13

c) ¿Cuál es la interfaz del módulo?

    principal.py
    
d) ¿Cuál es la implementación del módulo?

    fibonacci.py
    
"""

if len(sys.argv) < 2:
    if fib(8) == 21 and fib_iter(8) == 21: 
        print("fib(8) vale 21 (Correcto)\nfib_iter(8) vale 37 (incorrecto)")
    else: 
        print("El modulo no funciona correctamente.")     
else:
    if int(sys.argv[1]) > 9: 
        print(fib_iter(int(sys.argv[1])))
    else: 
        print(fib(int(sys.argv[1])))
        