"""
125. Dado el documento XML del ejercicio anterior, escribir un programa que elimine al
socio cuyo id sea 51 y guarde los cambios en el mismo archivo.

"""
import xml.etree.ElementTree as ET

xml_tree = ET.parse('bo121.xml')
root = xml_tree.getroot()
socios = root.find("socios")
socio_a_eliminar = socios.find("./socio[@id='5']")
socios.remove(socio_a_eliminar)
xml_tree.write('bo121.xml')