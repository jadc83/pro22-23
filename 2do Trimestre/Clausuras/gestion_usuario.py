from userconfig import *

def ayuda():
    print("-----------------------------------------------------------------------")
    print("OPCIONES DISPONIBLES:")
    print("-----------------------------------------------------------------------")
    print("crea_usuario(nombre, password)                     CREAR USUARIO.")
    print("listar()                                           LISTAR USUARIOS.")
    print("cambiar_pass(usuario, password, nuevo password)    CAMBIAR PASSWORD.")
    print("-----------------------------------------------------------------------")
    return ayuda
ayuda()