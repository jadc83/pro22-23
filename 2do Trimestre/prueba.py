def pareja(*args):
    if len(args) == 2:        
        def get(indice):
            a = args[0]
            if indice == 0:
                return a
            else:
                return "La contraseña es privada"
    elif len(args) == 3:
        def get(indice):
            a, b, c = args[0], args[1], args[2]
            if indice == 0:
                return a
            elif indice == 1:
                if c == "admin":
                    return b
            else:
                return "Indice incorrecto."            
    else:
        def get(indice):
            return "Numero de parametros incorrecto"

    return get

def select (funcion, indice):
        return funcion(indice)