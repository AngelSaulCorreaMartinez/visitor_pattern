from Visitante import Visitante

class EquiparArma(Visitante):
    def visitar_mago(self, mago):
        mago.set_arma('Daga')
        
    def visitar_guerrero(self, guerrero):
        guerrero.set_arma('Espada')

    def visitar_personajes(self, personajes):
        for personaje in personajes:
            personaje.aceptar(self)