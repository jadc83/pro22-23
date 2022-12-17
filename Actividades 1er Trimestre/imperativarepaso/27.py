"""
27. En el archivo numeros.txt disponemos de una serie de números (uno por línea). Diseñar
un programa que procese el archivo y nos muestre el menor y el mayor.
"""

with open("numeros.txt", "r", encoding="UTF-8") as fichero:
    nums = []
    LINEAS = fichero.readlines()
    nums += [int(x.strip()) for x in LINEAS]
    print(f"El minimo es {min(nums)} y el maximo es {max(nums)}")
