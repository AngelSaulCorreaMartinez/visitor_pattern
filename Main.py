from Guerrero import Guerrero
from Mago import Mago
from EquiparArma import EquiparArma
from EquiparEncantamiento import EquiparEncantamiento

def main():
    g1 = Guerrero()
    g2 = Guerrero()
    m1 = Mago()
    m2 = Mago()

    m1.set_nivel_magico(3)
    m2.set_nivel_magico(7)

    personajes = []
    personajes.append([g1, g2, m1, m2])

    ea = EquiparArma()
    ea.visitar_personajes(personajes)

    ee = EquiparEncantamiento()
    ee.visitar_personajes(personajes)

main()