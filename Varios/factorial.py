def factorial(num):
	i = 1
	for e in range(1, num + 1):
		i *= e
	return i


def series_resistance(lst):
	tipo = 1.2
	dec = [float(x) for x in lst]
	resultado = sum(dec)
	if type(resultado) != type(tipo):
		raise ValueError("El resultado no es float")
	if resultado < 2:
		print(str(resultado) + " " + "omh")
	else:
		print(str(resultado) + " " + "omhs")