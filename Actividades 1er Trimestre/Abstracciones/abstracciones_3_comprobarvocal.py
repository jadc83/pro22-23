"dasd"
vocales = ["a","e","i","o","u"]
esvocal = lambda x : x.translate(x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")).replace(" ","").lower() in\
    vocales if x != "" else "Cadena vacia"
