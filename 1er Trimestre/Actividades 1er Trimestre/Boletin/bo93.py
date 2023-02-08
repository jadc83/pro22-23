"""
93. El ayuntamiento de Sanlúcar te ha encargado una aplicación que ayude a realizar
encuestas estadísticas para conocer el nivel adquisitivo de los sanluqueños. Para ello,
tendrás que preguntar el sueldo a cada persona encuestada. A priori, no se conoce el
número de encuestados. Para finalizar la entrada de datos, introduce un sueldo con
valor −1.
Una vez terminada la entrada de datos, muestra la siguiente información:
• Todos los sueldos introducidos, ordenados de forma decreciente.
• El sueldo máximo y mínimo.
• La media de los sueldos.

"""
resultado = []
while True:
    salario = float(input("Introduce salario:\n"))
    if salario == -1:
        break
    else:
        resultado.append(salario)

if resultado == []:
    print("No existen salarios")
    print("Sin elementos")
else:
    print("SALARIOS")
    for x in resultado:
        print("------------------------------")
        print(x)
    print(f"Salario minimo:{min(resultado)}\nSalario Maximo:{max(resultado)}")
    print("-------------MEDIAS-----------")
    media = sum(resultado) / len(resultado)
    print(media)