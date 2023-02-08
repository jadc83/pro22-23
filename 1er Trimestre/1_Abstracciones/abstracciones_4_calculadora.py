"""Calculadora
x = primer operando
y = segundo operando
z = operador

"""

calcula = lambda x,y,z: x + y if z == '+' else \
    x - y if z == '-' else \
        x * y if z == '*' else \
            int(x / y) if z == '/' else "Tu que eres muy listo?"
