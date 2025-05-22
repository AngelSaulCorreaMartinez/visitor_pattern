from Visitable import Visitable

class Mago(Visitable):
    def __init__(self):
        self.__arma = ''
        self.__encantamiento = ''
        self.__nivel_magico = 1

    def get_arma(self): 
        return self.__arma 
    
    def set_arma (self, arma): 
        self.__arma = arma

    def get_encantamiento(self): 
        return self.__encantamiento
     
    def set_encantamiento(self, encantamiento): 
        self.__encantamiento = encantamiento 
    
    def get_nivel_magico(self):
        return self.__nivel_magico 

    def set_nivel_magico(self, nivel_magico): 
        self.__nivel_magico = nivel_magico

    def aceptar(self, visitante):
        visitante.visitar_mago(self)