"""
Modifica el formato de un dato "fecha", alternando entre el estilo europeo y el japones

"1994/07/19" -----> "19/07/1994"

"""
def conv_fecha(cadena):
    lista = cadena.split("/")[::-1]
    lista1 = "/".join(lista)
    return lista1