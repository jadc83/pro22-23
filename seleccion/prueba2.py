import xml.etree.ElementTree as ET
arbol = ET.parse('bo121.xml')
raiz = arbol.getroot()
lista = []
lista1 = []
socios = raiz.findall('./socios/')
for x in socios:
    ident = x.get('id')
    lista.append(ident)
socio = raiz.findall('./socios/socio')
for x in socio:
    nombre = x.find('nombre')
    lista1.append(nombre.text)

res = zip(lista,lista1)
diccionario = dict(res)
