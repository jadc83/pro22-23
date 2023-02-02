"""
Escribir en Python una función shows() sin argumentos que cargue el archivo 
«shows.xml» y que devuelva un diccionario donde:

Las claves serán los títulos de todas las películas y series (no los episodios) 
que tengan género «Fantasía».

Los valores asociados a cada clave serán el número de episodios que tiene la 
serie (si es una serie) o None si es una película.

"""

import xml.etree.ElementTree as ET

def shows():
    """shows"""
    resultado = []
    arbol = ET.parse("shows.xml")
    raiz = arbol.getroot()
    
    peliculas_fantasia = raiz.findall(".//pelicula[genero='Fantasía']")
    for elemento in peliculas_fantasia:
        clave = elemento.findtext("titulo")
        valor = 1
        resultado.append((clave, valor))

    series_fantasia = raiz.findall(".//serie[genero='Fantasía']")
    for elemento in series_fantasia:
        clave = elemento.findtext("titulo")
        episodios = raiz.findall(".//serie/temporada/episodio")
        resultado.append((clave, len(episodios)))
    
    resultado = dict(resultado)
print("Star Wars" in shows())

    