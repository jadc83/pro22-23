"""

23. Hacer el mismo ejercicio anterior, pero recogiendo el nombre del archivo desde la línea
de órdenes del sistema operativo. (Indicación: usar sys.argv).

"""

import sys

nombre = sys.argv[1] if len(sys.argv) == 2 else "pruebas.txt"

#############################################################

fichero = open(nombre, "r")
copiando = fichero.readlines()
fichero.close()

#############################################################

limpiando = [x.strip() for x in copiando]
dale = [print(x) for x in limpiando]


