"""
122. Dado el documento XML del ejercicio anterior, escribir un programa 
que cuente cuántos socios tiene el club y lo muestre por pantalla
"""

import xml.etree.ElementTree as ET
arbol = ET.parse('bo121.xml')
raiz = arbol.getroot()
contador = 0
for x in raiz.findall('./socios/socio'):
    contador += 1
print(contador) 