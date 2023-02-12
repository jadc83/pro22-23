class personaje:
    
    def __init__(self, nombre, fuerza, constitucion, tamaño, destreza, apariencia, inteligencia, educacion, poder):
        self.nombre = nombre
        self.FUE = fuerza
        self.CON = constitucion
        self.TAM = tamaño
        self.DES = destreza
        self.APA = apariencia
        self.INT = inteligencia
        self.EDU = educacion + 3
        self.POD = poder
        self.SUE = self.POD * 5
        self.HP = ( self.TAM + self.CON ) / 2
        self.MP = self.POD

    def atributos(self):
        print(".Nombre:", self.nombre)
        print(".FUE:", self.FUE)
        print(".CON:", self.CON)
        print(".TAM", self.TAM)
        print(".DES:", self.DES)
        print(".APA:", self.APA)
        print(".INT:", self.INT)
        print(".EDU:", self.EDU)
        print(".POD:", self.POD)
        print(".SUE", self.SUE)
        print(".HP", self.HP)
        
    def esta_vivo(self):
        return self.HP > 0
     
        
    def ataque(self, enemigo):
        enemigo.HP = enemigo.HP - ( self.FUE / 2 )
        if enemigo.HP > 1:
            print(enemigo.nombre,"recibe la ostia", "Vida restante:", enemigo.HP)
        else:
            print( enemigo.nombre, "ha muerto.")
            print(chr(27)+"[1;31m"+"Fatality") 
            print(chr(27)+"[1;31m"+"Flawless Victory.") 
            
            

       
