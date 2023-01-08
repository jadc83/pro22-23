FRASE = "Dábale arroz a la zorra el abad"
CONACENTO,SINACENTO = "áéíóú", "aeiou"
FILTRO = FRASE.maketrans(CONACENTO,SINACENTO)
F1 = FRASE.translate(FILTRO).lower().replace(" ","")
F2 = F1[::-1]



    

