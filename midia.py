from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id
    
    @abstractmethod
    def armazenar():
        pass

    @abstractmethod
    def buscaTudo():
        pass
    
    @abstractmethod
    def atualizar():
        pass

    @abstractmethod
    def deletar():
        pass
