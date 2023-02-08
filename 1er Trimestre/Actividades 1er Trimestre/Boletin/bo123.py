"""
Dado el documento XML del ejercicio anterior, escribir un programa que cambie la
dirección de todos los socios por «Avda. de Huelva, s/n» y guarde los cambios en el
mismo archivo.
"""
import xml.etree.ElementTree as ET
arbol = ET.parse('bo121.xml')
raiz = arbol.getroot()
for c in raiz.findall('./socios/socio'):
    print(c.get("estado", "Sin estado"))
for x in raiz.findall('./socios/socio/direccion'):
    print(x.text)
