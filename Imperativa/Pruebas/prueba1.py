"""#(input("Introduce mierda aqui: ") for x in range(1,11)[::-1])
acu = []
hola = (acu.append("x") for x in (input("Introduce mierda aqui: ") for x in range(1,11)))
print(list(acu))
"""
vacia = []
lista = [input("Mete aqui:") for x in range(1,11)]
mete = [vacia.append(x) for x in lista]
print(mete[::-1])

