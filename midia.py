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

class Serie(Filme):
    def __init__(self, tipo, id, titulo, direcao, ano, genero, sinopse):
        super().__init__(tipo, id, titulo, direcao, ano, genero, sinopse, episodios, produtora)
        self.episodios = episodios
        self.produtora = produtora
    
    def armazenar(self, obj):
        pass

    def buscaTudo(self):
        pass

    def assistir(self):
        pass

    def atualizar(self, id):
        pass

    def deletar(self, id):
        pass

