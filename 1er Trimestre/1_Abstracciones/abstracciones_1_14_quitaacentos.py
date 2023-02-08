"""
acentos = x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")
salida = x.translate(acentos)
"""

noacento = lambda x : "" if x == "" else x.translate(x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU"))
