"""asdasd"""
def ahorcado (palabra):
    """ahorcado"""
    fichero = open("ahorcado.txt", "r")
    linea = fichero.readline()
    fichero.close()
    lista = []
    if linea == palabra.upper():
        print("¡Enhorabuena!")
    else:
        for x in linea.upper():
            if x in palabra.upper():
                lista.append(x)
            else:
                lista.append("_")
        lista = "".join(lista)
        print(lista)

from itertools import count
unico = lambda sec, ac1, cont: set(ac1) if cont == len(sec) else \
    unico( sec, ac1 + [sec[cont]], cont + 1) if sec.count(sec[cont]) < 2 else \
        unico( sec, ac1 ,cont + 1)

cadena = ['perro=guau', 'gato=miau', 'vaca=mu']

def str2dic(lista):
    lista = [x.split("=") for x in lista]
    return dict(lista)