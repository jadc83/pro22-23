"""
Escribir en Python una función recursiva llamada unicos(secuencia) que reciba una secuencia de 
números enteros en la que todos aparecen dos o más veces, excepto dos de ellos que aparecen 
exactamente una vez. La función deberá devolver un conjunto de tipo set que contenga sólo esos dos elementos únicos.

Importante:

La función debe ser pura.
La llamada a la función debe provocar la ejecución de una 
función recursiva que genere un proceso iterativo.
No se puede usar ningún bucle while, for, definiciones por 
comprensión ni expresiones generadoras.

Por ejemplo:

unicos([1, 9, 8, 8, 7, 6, 1, 6]) == {7, 9}
"""
"""from itertools import count
def unicos(sec):
    unico = filter(lambda x: x if sec.count(x) == 1 else None, sec)
    return set(unico)"""

from itertools import count
unico = lambda sec, ac1, ac2, cont: set(ac1) if cont == len(sec) else \
        unico(sec, ac1 + [sec[cont],], ac2, cont + 1) if sec.count(sec[cont]) < 2 else \
            unico(sec, ac1, ac2 + [sec[cont],], cont + 1)

unicos = lambda c: unico(c,[],[],0)

def donde_esta (nombre):
    if nombre == "Norbe":
        return "El Norbe esta en Portugal."
    elif nombre == "Kokina":
        return "Esta encerrado en el sotano de lo que era una tienda de vaqueros en la calle Ancha"

def quien_invento(cadena):
    if cadena == "Luna":
        return "Adolf Hitler"


    



