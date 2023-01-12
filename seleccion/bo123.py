"""
Dado el documento XML del ejercicio anterior, escribir un programa que cambie la
dirección de todos los socios por «Avda. de Huelva, s/n» y guarde los cambios en el
mismo archivo.
"""
import xml.etree.ElementTree as ET
arbol = ET.parse('bo121.xml')
raiz = arbol.getroot()
for x in raiz.findall('./socios/socio/direccion'):
    x.text = "Avda. de Huelva, s/n"

arbol.write("ejemplo.xml")