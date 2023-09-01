class Instrumento():
    
    def __init__(self):
        self.nombre=str
        self.afina=bool

    def afinar (self):
        if self.afina==False:
            return 0
        else:
            print("Afinando"+ self.nombre)
    
    def tocar(self):
        self.nombre=str
        print("Tocando"+self.nombre)

