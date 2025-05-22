import abc

class Visitante(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def visitar_mago(self, mago): pass

    @abc.abstractmethod
    def visitar_guerrero(self, guerrero): pass

    @abc.abstractmethod
    def visitar_personajes(self, personajes): pass