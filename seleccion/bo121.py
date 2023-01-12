"""
121. Dado un documento XML similar a éste (es decir, con la misma estructura 
pero no necesariamente con el mismo contenido) y almacenado en el archivo 
club.xml:

Escribir un programa que muestre los socios del club de forma similar a la 
siguiente:

[1] Sherlock Holmes
[51] Winston Churchill


"""

import xml.etree.ElementTree as ET
arbol = ET.parse('bo121.xml')
raiz = arbol.getroot()

for x in raiz.findall('./socios/socio'):
    ident = x.get('id')
    socios = x.find('nombre').text
    print(f"[{ident}] {socios}")


    