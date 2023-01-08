"""
La calificación máxima del examen es de 7 puntos.
Los ejercicios no deben tener ningún error de estilo, lo que se comprueba mediante:
pylint --disable=invalid-name,redefined-outer-name,unnecessary-lambda-assignment
Hasta que el ejercicio no supere todas las comprobaciones de pylint, no se llevan a cabo las comprobaciones de los tests.
Por cada test superado: se suman T puntos, siendo T la cantidad de tests que tiene el ejercicio.
Posteriormente, se hará una comprobación manual para realizar las siguientes verificaciones (siendo P la puntuación total del ejercicio):
Por cada test superado usando un algoritmo ad-hoc: se restan T puntos.
Por cada algoritmo incorrecto utilizado: se restan P2 puntos.
Por cada detalle algorítmico innecesariamente complicado o ineficiente: se restan P4 puntos.

(Un algoritmo ad-hoc es aquel que está diseñado maliciosamente para superar un test, devolviendo directamente la salida esperada por el test ante los valores de entrada adecuados. Por ejemplo, una función que debería calcular la suma de dos números pero que lo único que hace es devolver directamente 7 ante los argumentos 4 y 3 para superar el test suma(4, 3) == 7.)

Criterios de evaluación:

CE1.a CE1.b CE1.c CE1.d CE1.e CE1.f CE1.g CE1.h CE1.i

CE2.b CE2.d CE2.f CE2.g CE2.i

CE3.a CE3.b CE3.c CE3.d CE3.e CE3.f CE3.g

CE5.a CE5.b CE5.c CE5.d CE5.e

CE6.c CE6.d CE6.e CE6.g CE6.h CE6.i
"""