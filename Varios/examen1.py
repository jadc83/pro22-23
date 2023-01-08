"""
Escribir en Python una función pura llamada intercambiar(persona)
que reciba una cadena con el nombre (que puede ser compuesto) y los
apellidos (que también pueden ser compuestos) de una persona,
en ese orden y separados por exactamente dos espacios en blanco,
y los devuelva en una cadena poniendo primero los apellidos y
después el nombre, separados por «,␣» (una coma y un espacio).

Si la cadena recibida no tiene la forma requerida,
debe devolverla tal cual sin modificar.

En la cadena recibida no puede haber números ni otros
signos de puntuación salvo los espacios en blanco.
"""

aux = lambda t: () if t == () else \
    aux(t[1:]) + (t[0],)

intercambiar = lambda n: n if len(tuple(n.split("  "))) != 2 else \
    aux(tuple(n.split("  ")))[0] + ", " + tuple(n.split("  "))[0]



