vacia = [] #Lista vacia que se usara para meter los inputs
inputasiones = [input("Mete aqui:") for x in range(1,5)] #Recogida de datos por teclado
mete = [vacia.append(cadena) for cadena in inputasiones] #Aqui se van añadiendo los elementos a la lista vacia
llena = vacia[::-1] #Se hace una copia de la lista pero en orden inverso

#En este punto la lista ya esta creada

archivo = open("prueba.txt", "a") #Se abre el archivo en modo añadir
archivo.write(str(llena) ) #Se escribe el contenido de la lista al final del archivo
archivo.close() #Se cierra el archivo y se comprueba el contenido con cat.
