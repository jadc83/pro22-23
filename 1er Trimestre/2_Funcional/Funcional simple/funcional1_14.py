"dasdasd"
FRASE = "!Ramón! !Cuánto tiempo! ¿Cómo estás?"
acentos = FRASE.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")
salida = FRASE.translate(acentos)
