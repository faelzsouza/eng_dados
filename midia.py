from abc import ABC, abstractmethod
import pygame
from time import sleep

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

    @abstractmethod
    def buscaTudo():
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
        listaSeries.append(vars(obj))

    def assistir(self, index):
        print(f'Você está assistindo t01ep01 de {listaSeries[index]["titulo"]}...')
        pygame.init()
        pygame.mixer.music.load('nouveau-jingle-netflix.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        sleep(5)

    def atualizar(self, index, chave, valor):
        listaSeries[index][chave] = valor

    def deletar(self, index):
        listaSeries.pop(index)
    
    def buscaTudo(self):
        for i, s in enumerate(listaSeries):
            print(f'[{i+1}] {listaSeries[i]["titulo"]}') # Mostra as séries que estão na lista!

listaSeries = []
id = 0
while True:
    print('''[1] Adicionar Série
[2] Assistir Série
[3] Atualizar Série
[4] Deletar Série
[0] Sair do Programa''')
    r = int(input())
    if r == 1:
        print('Titulo: ')
        titulo = input()
        if titulo == '0':
            break
        print('Direção: ')
        direcao = input()
        print('Ano: ')
        ano = int(input())
        print('Genero: ')
        genero = input()
        print('Sinopse: ')
        sinopse = input()
        print('Episódios: ')
        ep = int(input())
        print('Produtora: ')
        prod = input()
        serie = Serie('visual', id, titulo, direcao, ano, genero, sinopse, ep, prod)
        serie.armazenar(serie)
        id += 1
    elif r == 2:
        print('Qual série deseja assistir?')
        serie.buscaTudo()
        serie.assistir(int(input()) - 1)
    elif r == 3:
        print('Qual série deseja editar?')
        serie.buscaTudo()
        index = int(input()) - 1
        print(f'O que você deseja editar em {listaSeries[index]["titulo"]}?')
        for i, k in enumerate(listaSeries[index].keys()):
            if i > 1:
                print(f'[{i - 1}] {k.capitalize()}')
        key = int(input()) + 1
        key = list(listaSeries[index].keys())[key]
        print(f'Você deseja alterar {key.capitalize()}: {listaSeries[index][key]} para qual valor?')
        valor = input()
        serie.atualizar(index, key, valor)
    elif r == 4:
        print('Qual série deseja deletar?')
        serie.buscaTudo()
        index = int(input()) - 1
        serie.deletar(index)
    else:
        break

print('FIM')