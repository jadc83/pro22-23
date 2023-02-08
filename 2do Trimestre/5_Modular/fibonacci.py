"""
4. Escribe un módulo llamado fibonacci.py que contenga las siguientes funciones:

    • Una función fib que calcule el 𝑛-ésimo término de la sucesión de Fibonacci de
        forma recursiva.
        
    • Una función fib_iter que calcule lo mismo pero de forma iterativa llamando a
        otra función _fib_aux (ojo, que empieza por _), que es la que realmente lleva a
        cabo el proceso iterativo.
"""


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    

def _fib_aux(contador, a, b):
    if contador == 0:
        return a
    else:
        return _fib_aux(contador - 1, b, a + b)


def fib_iter(n):
    return _fib_aux(n, 0, 1)
