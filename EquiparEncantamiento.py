from Visitante import Visitante

class EquiparEncantamiento(Visitante):
    def visitar_mago(self, mago):
        if mago.get_nivel_magico() <= 5:
            mago.set_encantamiento('Bola de fuego')
        else:
            mago.set_encantamiento('Rayo de hielo')
        
    def visitar_guerrero(self, guerrero):
        pass

    def visitar_personajes(self, personajes):
        for personaje in personajes:
            personaje.accept(self)