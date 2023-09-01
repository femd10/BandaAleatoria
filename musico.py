from instrumentos import Instrumento



class Musico():
    def __init__(self,instrumento):
        self.instrumento=instrumento
    def afinar(self):
        self.instrumento.afinar()
    def tocar(self):
        self.instrumento.tocar()
        