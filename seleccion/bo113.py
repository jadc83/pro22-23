"""
113. Realizar el juego del ahorcado. Las reglas del juego son:
a. El jugador A teclea una palabra, sin que el jugador B la vea.
b. Ahora se le muestran tantos guiones como letras tenga la palabra secreta. Por
ejemplo, para «hola» se mostraría «----».
c. El jugador B intentará acertar, letra a letra, la palabra secreta.
d. Cada acierto muestra la letra en su lugar, y las letras no acertadas seguirán ocultas como guiones. Siguiendo con el ejemplo anterior, y suponiendo que se ha
introducido la «o», la «j» y la «a», se mostrará «-o-a».
e. El jugador B sólo tiene 7 intentos.
f. La partida terminará al acertar todas las letras que forman la palabra secreta (gana
el jugador B) o cuando se agoten todos los intentos (gana el jugador A).
"""
import getpass
adivina = getpass.getpass(prompt='Introduce la palabra: ', stream=None)
guiones = ["_" for x in adivina]
lista = dict(list(enumerate(adivina)))
contador = 7

while contador > 0:
    if contador != 0:
        print("".join(guiones))
        if "".join(guiones) == adivina:
            print("Gana el jugador B")
            break
        else:
            intento = input("Mete letra:")
            for key,value in lista.items():
                if value == intento:
                    guiones[key] = intento
            contador -= 1
            if contador < 1:
                print("Gana el jugador A")
        