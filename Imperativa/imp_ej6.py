"""
6. Escribe un programa que pida el año actual y el de nacimiento del usuario. Debe calcular
su edad, suponiendo que en el año en curso el usuario ya ha cumplido años.

"""

#finales = lambda n, t: t if len(t) == n else finales(n,t[1:])

actual = int(input('En que año estamos?\n'))
print('Vale.')
nacimiento = int(input('Y en que año naciste?\n'))
print('Ok pos...')
edad = actual - nacimiento
print('Pues tienes ' + str(edad) + ' años')