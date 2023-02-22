def crear_usuario(nombre, password):
    """Esta funcion usa a su vez la funcion 'createuser' del 
       modulo 'creacion_usuario.py' para su funcionamiento."""
    def usuario():
        tupla = nombre, password
        return dict((usr, pwd) for usr, pwd in [tupla])
    return usuario
