import abc

class Visitable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def aceptar(self, visitante): pass