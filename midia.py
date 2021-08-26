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

class Filme(Midia):
  def _init_(self,tipo,id,titulo,direcao,ano,genero,sinopse):
    super().__init__(tipo,id)
    self.titulo = titulo
    self.direcao = direcao
    self.ano = ano
    self.genero = genero
    self.sinopse = sinopse

    
    def armazenar():
        pass
    
   
    def buscaTudo():
        pass
    
  
    def assistir():
        pass
    

    def deletar():
        pass
    

    def atualizar():
        pass
