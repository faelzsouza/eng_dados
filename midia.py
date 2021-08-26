from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id
    
    @abstractmethod
    def armazenar():
        pass
    
    @abstractmethod
    def atualizar():
        pass

    @abstractmethod
    def deletar():
        pass

class Filme(Midia):
    def __init__(self,tipo,id,titulo,direcao,ano,genero,sinopse):
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


class Serie(Filme):
    def __init__(self, tipo, id, titulo, direcao, ano, genero, sinopse, episodios, produtora):
        super().__init__(tipo, id, titulo, direcao, ano, genero, sinopse)
        self.episodios = episodios
        self.produtora = produtora
    
    def armazenar(self, obj):
        pass

    def assistir(self):
        pass

    def atualizar(self, id):
        pass

    def deletar(self, id):
        pass

listaSeries = []

serie = Serie('visual', 1, 'Dark', 'Não sei', 2019, 'Suspense', 'Muito Bom!', 20, 'Também não sei')
print(vars(serie))