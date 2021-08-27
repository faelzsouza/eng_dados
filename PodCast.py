# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:26:29 2021

@author: danie
"""


from abc import ABC, abstractmethod
from time import sleep
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


class Podcast(Midia): #classe feita visando orientação pelos pontos que destacam um podcast trazendo da class padrão
    def __init__(self, tipo, id, titulo, host, episodios):
        super().__init__(tipo, id)
        self.titulo = titulo
        self.host = host
        self.episodios = episodios
        

    
    def armazenar(self, objeto): #armazena o objeto em formato de dicionário dentro da lista
        listaPodcasts.append(vars(objeto))

    
    def buscaTudo(self): #mostra no console todos os itens da lista pelo título do dicionário
        for n, x in enumerate(listaPodcasts):
            print(f'[{n+1}] {listaPodcasts[n]["titulo"]}')
    
    
    def assistir(self, index): #mostra pro user o que ele tá assistindo
        print('Você está assistindo {}'.format(listaPodcasts[index]['titulo']))
        sleep(5)

    
    def deletar(self, index): #apaga um dicionário da lista que é especificado pelo index 
        listaPodcasts.pop(index)

    
    def atualizar(self, index, chave, valor): #atualiza uma chave de um dicionário específico da lista
        listaPodcasts[index][chave] = valor
    
    


listaPodcasts = []
id = 0
while True: #feito um laço de repetição para também proteger o code de quebrar por algum erro do user 
    print('''[1] Adicionar um Podcast?
          [2] Assistir um Podcast?
          [3] Atualizar algum Podcast?
          [4] Deletar um Podcast?
          [0] Sair do formulário''')
    while True:
        try:
            n = int(input('Digite uma opção: '))
            if n < 0 or n > 4:
                print('Opção inválida! ')
            else:
                break
        except:
                  print('Digite apenas opções válidas por favor! ')
   
    if n == 1: #parte do menu para adicionar um podcast
        print('Qual o título do Podcast?  ')
        titulo = input('Título: ')
        if titulo == 0:
            break
        print('Host: ')
        host = input('Quem são os(as) anfitriões(ãs) do progama? ')
        print('Episódio: ')
        episodios = input()
        Podcast = Podcast('audio', id, titulo, host, episodios)
        Podcast.armazenar(Podcast)
        id += 1
    elif n == 2:# parte do menu de para assistir um episódio
        print('Qual episódio gostaria de assistir? ')
        for n, x in enumerate(listaPodcasts):
            print(f'[{n+1}] {listaPodcasts[n]["titulo"]}')
        Podcast.assistir(int(input()) -1)
    elif n == 3: #parte do menu para edição de alguma chave
        print('Qual Podcast deseja editar? ')
        Podcast.buscaTudo()
        index = int(input()) - 1
        print(f'O que deseja editar em {listaPodcasts[index]["titulo"]} ?')
        for x, k in enumerate(listaPodcasts[index].keys()):
            if x > 1:
                print(f'[{x - 1}] {k.capitalize()}')
        key = int(input()) + 1
        key = list(listaPodcasts[index].keys())[key]
        print(f'Você deseja alterar {key.capitalize()}: {listaPodcasts[index][key]} para? ')
        valor = input()
        Podcast.atualizar(Podcast)
    elif n == 4: #deletar um podcast
        print('Qual Podcast deseja deletar? ')
        Podcast.buscaTudo()
        Podcast.deletar(int(input()))
        
        
    else:
        break #finalização do programa

print('Fim do programa. ')




       
