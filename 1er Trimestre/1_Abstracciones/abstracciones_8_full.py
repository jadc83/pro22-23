"""
a) Explicar brevemente que hace el programa.
b) Determinar los ambitos que hay en el codigo fuente.
c) Indicar:
        1. Los parametros
        2. Los ligaduras locales, y de que ambito son locales.
        3. Las ligaduras globales.
d) Trazar su ejecucion paso a paso, indicando el contenido de la pila,
   el entorno y las ligaduras que se van creando y destruyendo durante la
   ejecucion.
   
   1) Se crea la ligadura producto -- lambda en Global
   2) Se crea la ligadura cuenta -- lambda en Global
   3) Se crea la ligadura resultado y se evalua producto
   4) Se entra al ambito de producto y se crea un nuevo marco
      sobre el marco global (Entorno: producto apunta a global)
   5) Se crea la ligadura x -- 2 en ambito de producto()
   6) Se crea la ligadura y -- 3 en ambito de producto()
   7) Se evalua x devolviendo 2
   8) Se evalua y devolviendo 3
   9) Se evalua 2 * 3 y devuelve 6
   10) Se destruye el marco producto (Entorno: Marco global)
   11) Se entra al ambito de cuenta y se crea un nuevo marco sobre
       el marco producto() (Entorno: cuenta apunta a global )
   12) Se crea la ligadura x -- 'amapola'.count('a')
   13) Se evalua 'amapola'.count('a') y devuelve 2
   14) Se sale del marco cuenta (Entorno: Marco global)
   15) Se evalua 6 + 2 y devuelve 8
"""

producto = lambda x,y: x * y
cuenta = lambda x: x.count('a')
resultado = producto(2,3) + cuenta('Amapola')
