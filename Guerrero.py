from Visitable import Visitable

class Guerrero(Visitable):

    def __init__(self):
        self.__arma = ''

    def get_arma(self):
        return self.__arma
    
    def set_arma(self, arma):
        self.__arma = arma
    
    def aceptar(self, visitante):
        visitante.visitar_guerrero(self)