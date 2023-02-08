long_tibia = 38.42
sexo = "V"
edad = 32

aprox = 69.089 + ( 2.232 * long_tibia) if sexo == "V" else \
         61.412 + ( 2.317 * long_tibia )
    
altura =  aprox if edad <= 30 else aprox - (0.06 * (edad - 29))
