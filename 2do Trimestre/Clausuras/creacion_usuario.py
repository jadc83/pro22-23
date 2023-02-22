from tad import crear_usuario

__usuarios = dict()

def createuser(nombre, password):
    """Genera el usuario con los parametros asignados 
       y lo agrega a la lista de usuarios"""
    user = crear_usuario(nombre, password)
    __usuarios.update(user())

def listar_usuarios():
    if len(__usuarios) == 0:
        return "No existen usuarios en el sistema."
    else:
        for x in __usuarios.keys():
            print(x)

def cambiar_pass(usuario, password, nuevo):
    if password == __usuarios[usuario]:
        print("Password actualizado.")
        return createuser(usuario,nuevo)
    else:
        return "Password incorrecto."