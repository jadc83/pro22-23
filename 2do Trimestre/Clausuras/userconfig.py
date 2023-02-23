__usuarios = dict()

def gestion_usuario():
    
    def genera(nombre, password):
        """Esta funcion usa a su vez la funcion 'createuser' del 
        modulo 'creacion_usuario.py' para su funcionamiento."""
        def usuario():
            tupla = nombre, password
            return dict((usr, pwd) for usr, pwd in [tupla])
        return usuario

    def crear_usuario(nombre, password):
        """Genera el usuario con los parametros asignados 
        y lo agrega a la lista de usuarios"""
        user = genera(nombre, password)
        __usuarios.update(user())
        print("Usuario creado con exito.")
        
    def listar_usuarios():
        if len(__usuarios) == 0:
            return "No existen usuarios en el sistema."
        else:
            for x in __usuarios.keys():
                print(x)
    
    def cambiar_pass(usuario, password, nuevo):
        if password == __usuarios[usuario]:
            __usuarios[usuario] = nuevo
            print("Password actualizado.")
        else:
            return "Password incorrecto." 

    return genera, crear_usuario, listar_usuarios, cambiar_pass

genera, crea_usuario, listar, cambiar_pass = gestion_usuario()