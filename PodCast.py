# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:26:29 2021

@author: danie
"""


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


class Podcast(Midia):
    def __init__(self, tipo, id, titulo, host, episodios):
        super().__init__(tipo, id)
        self.titulo = titulo
        self.host = host
        self.episodios = episodios
        

    
    def armazenar(self, objeto):
        listaPodcasts.append(vars(objeto))

    
    def buscaTudo():
        pass
    
    
    def assistir():
        pass

    
    def deletar():
        pass

    
    def atualizar():
        pass




listaPodcasts = []
FlowPodcast = Podcast('Podcast', 1, 'PSIU - Flow Podcast #448', 'Igão e Monark', 448)
FlowPodcast.armazenar(FlowPodcast)
print(listaPodcasts)       

    