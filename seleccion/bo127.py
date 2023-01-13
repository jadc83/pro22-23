"""
127. Dado el documento XML del ejercicio anterior, escribir un programa que muestre el
nombre de los socios por orden cronológico según su fecha de alta, de más antiguo a
más reciente.

"""

import xml.etree.ElementTree as ET
arbol = ET.parse('bo121.xml')
raiz = arbol.getroot()
l1 = []
l2 = []

nombres = raiz.findall('./socios/socio[nombre]')
for nombre in nombres:
    name = nombre.find('nombre')
    fecha = nombre.find('alta')
    l1.append(fecha.text)
    l2.append(name.text)
res = sorted(list(zip(l1,l2)))
for x, y in res:
    print(x,y)
