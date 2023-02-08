"""
5. Los médicos forenses utilizan la longitud de los huesos para determinar la altura de una
persona, cuando la persona estaba viva.
Por ejemplo, para los varones:

altura (en cm) = 69.089 + 2.232 × longitud de la tibia

Para las mujeres, el valor es el siguiente:
altura (en cm) = 61.412 + 2.317 × longitud de la tibia

A partir de los 30 años (inclusive), la altura de una persona decrece a una tasa de 0.06
cm por año.
Escribir un programa que, dados los valores de la longitud de la tibia, el sexo y la edad
del paciente, nos calcule la altura aproximada
"""
edad = 21
decrece = (edad - 30) * 0.06 if edad >= 30 else 0
tibia = 50
sexo = "V"

alturah= 69.089 + 2.232 * tibia
alturam= 61.412 + 2.317 * tibia

altura = round((alturah - decrece if sexo == "V" else alturam - decrece) , 2)
