def gestion_usuario():
    """Esta funcion contiene un diccionario '__usuarios' que contiene la
    informacion de los usuarios y a las funciones, 'genera()', 'crear_usuario()'
    'listar_usuario()' y 'cambiar_pass()' y a su vez las devuelve, luego 
    estas son asignadas en la asignacion multiple de genera, crear_usuario
    listar_usuarios y cambiar_pass"""
    
    __usuarios = dict()
    
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
        if user() not in __usuarios:
            __usuarios.update(user())
            print("Usuario creado con exito.")
        else:
            print("El usuario ya existe.")
        
    def listar_usuarios():
        """Lista los usuarios existentes en el sistema."""
        
        if len(__usuarios) == 0:
            return "No existen usuarios en el sistema."
        else:
            for x in __usuarios.keys():
                print(x)
    
    def cambiar_pass(usuario, password, nuevo):
        """Cambia la contraseña de un usuario, es necesario el password"""
        
        if password == __usuarios[usuario]:
            __usuarios[usuario] = nuevo
            print("Password actualizado.")
        else:
            return "Password incorrecto." 

    return genera, crear_usuario, listar_usuarios, cambiar_pass

genera, crea_usuario, listar, cambiar_pass = gestion_usuario()