"""
105. Los habitantes de Pythonlandia tienen un idioma algo extraño: cuando hablan, siempre
comienzan sus frases con «Pythonín, pythonón», para después hacer una pausa más
o menos larga (la pausa se representa mediante espacios en blanco o tabuladores) y a
continuación expresan el mensaje. Existe un dialecto que no comienza sus frases con la
muletilla anterior, pero siempre las terminan con un silencio, más o menos prolongado,
y la coletilla «pythonén, nen, nen». Se pide diseñar un traductor que, en primer lugar,
nos diga si la frase introducida está escrita en el idioma de Pythonlandia (en cualquiera
de sus dialectos) y, en caso afirmativo, nos muestre sólo el mensaje sin muletillas.

"""

import re
texto = input("Frase:\n")

patron = re.findall('^Pythonin, pythonon', texto)

if patron == []:
    print("No esta")
else:
    
    contenido = texto.split("     ")[1].strip()
