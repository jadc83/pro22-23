#def sumar(a, b):
#    def validar():
#        if a < 1 and b < 1:
#            return False
#        else:
#            return True
#    if validar() == True:
#        return a + b
    
#resultado = sumar(1, 2)
#print(resultado)
password1 = ""
password2 = "admin"
def credenciales(*credenciales):
    global password1
    password1 += credenciales[1]
    if len(credenciales) == 2:
        def separar(indice):
            nombre = credenciales[0]
            userpwd = credenciales[1]
            if indice == 0:
                return nombre
            elif indice == 1:
                vacio = ""
                for x in str(userpwd): vacio += "*"
                return vacio 
            else:
                return "Acceso denegado"
        return separar
            
    if len(credenciales) == 3:
        def separar(indice):
            nombre = credenciales[0]
            userpwd = credenciales[1]
            adminpwd = credenciales[2]
            if credenciales[2] == password2:
                if indice == 0:
                    return nombre
                elif indice == 1:
                    return userpwd
                elif indice == 2:
                    return "No es posible consultar el password."
        return separar
    print(password1)

separar = credenciales("jose","12345")




