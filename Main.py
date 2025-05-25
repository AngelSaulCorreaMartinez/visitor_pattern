# Importamos las clases necesarias para nuestro juego
from Guerrero import Guerrero
from Mago import Mago
from EquiparArma import EquiparArma
from EquiparEncantamiento import EquiparEncantamiento

def main():
    # Creamos instancias de nuestros personajes
    g1 = Guerrero()
    g2 = Guerrero()
    m1 = Mago()
    m2 = Mago()    # Configuramos los niveles mágicos de los magos
    m1.set_nivel_magico(3)  # Mago con nivel bajo (recibirá Bola de Fuego)
    m2.set_nivel_magico(7)  # Mago con nivel alto (recibirá Rayo de Hielo)

    # Creamos la lista de personajes
    personajes = []
    personajes.extend([g1, g2, m1, m2])

    # Creamos y aplicamos el visitante para equipar armas
    ea = EquiparArma()
    ea.visitar_personajes(personajes)

    ee = EquiparEncantamiento()
    ee.visitar_personajes(personajes)

    mostrar_info(personajes)

def mostrar_info(personajes):
    """
    Función que muestra la información de cada personaje.
    Para todos los personajes muestra su arma.
    Para los magos además muestra su encantamiento y nivel mágico.
    """
    for personaje in personajes:
        # Mostramos el arma que tiene equipada (todos los personajes tienen arma)
        print(f'Arma: {personaje.get_arma()}')
    
        # Verificamos si el personaje es una instancia de Mago para mostrar info adicional
        if isinstance(personaje, Mago):
            print(f'Encantamiento: {personaje.get_encantamiento()}')
            print(f'Nivel Magico: {personaje.get_nivel_magico()}')

            print('')
main()