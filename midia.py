from abc import ABC, abstractmethod
import pygame
from time import sleep


class Midia(ABC):  # Classe mãe/pai
    def __init__(self, tipo, id):
        self.__tipo = tipo
        self.__id = id

    # Métodos abstratos
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

    @abstractmethod
    def reproduzir():
        pass

class Filme(Midia):   # CLASSE FILHA DE MIDIA
    def __init__(self, tipo, id, titulo, direcao, ano, genero, sinopse):
        super().__init__(tipo, id)
        self.titulo = titulo
        self.direcao = direcao
        self.ano = ano
        self.genero = genero
        self.sinopse = sinopse

    def armazenar(self, object):  # METHOD ARMAZENAMOS O O FILME DESEJADO A LISTA
        listaFilmes.append(vars(object))

    def reproduzir(self, index):  # AQUI ESCOLHEMOS O FILME DESEJADO E ASSISTIMOS
        print(
            f'Você está assistindo o filme {listaFilmes[index]["titulo"]}...')
        pygame.init()
        pygame.mixer.music.load('nouveau-jingle-netflix.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        sleep(5)

    def atualizar(self, index, key, value):  # AQUI SE ALTERA FILMES JÁ ADICIONADOS E ATUALIZA
        listaFilmes[index][key] = value

    def deletar(self, index):  # METHOD PARA DELETAR FILMES DA LISTA
        listaFilmes.pop(index)

    def buscaTudo(self):
        for i, f in enumerate(listaFilmes):
            # MOSTRA OS FILMES DA LISTA
            print(f'[{i+1}] {listaFilmes[i]["titulo"]}')


class Serie(Filme):  # Classe série herda de Filme que herda de Midia
    def __init__(self, tipo, id, titulo, direcao, ano, genero, sinopse, episodios, produtora):
        super().__init__(tipo, id, titulo, direcao, ano, genero, sinopse)
        self.episodios = episodios
        self.produtora = produtora

    def armazenar(self, obj):
        listaSeries.append(vars(obj))

    def reproduzir(self, index):
        print(
            f'Você está assistindo T01EP01 de {listaSeries[index]["titulo"]}...')
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
            # Mostra as séries que estão na lista!
            print(f'[{i+1}] {listaSeries[i]["titulo"]}')


class Podcast(Midia):  # classe feita visando orientação pelos pontos que destacam um podcast trazendo da class padrão
    def __init__(self, tipo, id, titulo, host, episodios):
        super().__init__(tipo, id)
        self.titulo = titulo
        self.host = host
        self.episodios = episodios

    def armazenar(self, objeto):  # armazena o objeto em formato de dicionário dentro da lista
        listaPodcasts.append(vars(objeto))

    def buscaTudo(self):  # mostra no console todos os itens da lista pelo título do dicionário
        for n, x in enumerate(listaPodcasts):
            print(f'[{n+1}] {listaPodcasts[n]["titulo"]}')

    def reproduzir(self, index):  # mostra pro user o que ele tá assistindo
        print('Você está assistindo {}'.format(listaPodcasts[index]['titulo']))
        sleep(5)

    def deletar(self, index):  # apaga um dicionário da lista que é especificado pelo index
        listaPodcasts.pop(index)

    # atualiza uma chave de um dicionário específico da lista
    def atualizar(self, index, chave, valor):
        listaPodcasts[index][chave] = valor


class Musicas(Midia):
    '''Classe para seleção de musicas '''

    def __init__(self, tipo, id, artista, album, ano, genero, titulo):  # Método construtor da classe
        super().__init__(tipo, id)
        self.artista = artista
        self.album = album
        self.ano = ano
        self.genero = genero
        self.titulo = titulo

    def armazenar(self, item):
        listaMusica.append(vars(item))

    def atualizar(self, index, key, valor):
        listaMusica[index][key] = valor

    def deletar(self, index):
        print(f'A Música {listaMusica[index]["titulo"]} foi deletada!')
        listaMusica.pop(index)

    def buscaTudo(self):  # metodo para listar todas as músicas
        for i, m in enumerate(listaMusica):
            print(f'[{i+1}] {listaMusica[i]["titulo"]}')

    def reproduzir(self, index):
        print(f'Tocando {listaMusica[index]["titulo"]} de {listaMusica[index]["artista"]}')
        sleep(5)


# Listas para armazenamento
listaFilmes = []
listaSeries = []
listaPodcasts = []
listaMusica = []

id_filme = 0
id_serie = 0
id_musica = 0
id_podcast = 0

while True:
    while True:
        try:
            print(f'''{"-"*10} Bem-vindo(a) ao SoulFlix {"-"*10}
Qual mídia?
[1] Filmes
[2] Séries
[3] Músicas
[4] Podcasts
[0] Sair''')
            r = int(input())
            break
        except:
            print('\n Digite um número inteiro! \n')
    if r == 1:
        print(f'{"-" * 10} FILMES {"-" * 10}')
        while True:
            print('''[1] Adicionar Filme
[2] Assistir Filme
[3] Atualizar Filme
[4] Deletar Filme
[0] Menu inicial''')
            a = int(input())
            if a == 1:  # MENU PARA ADICIONAR FILME
                print('Título: ')
                titulo = input()
                if titulo == '0':
                    break
                print('Direção: ')
                direcao = input()
                print('Ano: ')
                ano = int(input())
                print('Gênero: ')
                genero = input()
                print('Sinopse: ')
                sinopse = input()
                filme = Filme('visual', id_filme, titulo,
                              direcao, ano, genero, sinopse)
                filme.armazenar(filme)
                id_filme = + 1
            elif a == 2:  # MENU PARA ESCOLHER E ASSISTIR O FILME
                print('Qual filme deseja assistir?')
                filme.buscaTudo()
                index = int(input())
                filme.reproduzir(index-1)

            elif a == 3:  # MENU PARA ALTERAR FILMES JÁ ADICIONADOS
                print('Qual filme deseja atualizar?')
                filme.buscaTudo()
                index = int(input())-1
                print(
                    f'O que você deseja editar em {listaFilmes[index]["titulo"]}')
                for i, k in enumerate(listaFilmes[index].keys()):
                    if i > 1:
                        print(f'[{i-1}] {k.capitalize()}')
                key = int(input())+1
                key = list(listaFilmes[index].keys())[key]
                print(
                    f'Você deseja alterar {key.capitalize()}: {listaFilmes[index][key]} para qual valor?')
                value = input()
                filme.atualizar(index, key, value)

            elif a == 4:
                print('Qual filme deseja excluir?')
                filme.buscaTudo()
                filme.deletar(int(input())-1)
            else:
                break
    elif r == 2:
        print(f'{"-" * 10} SÉRIES {"-" * 10}')
        # Menu série
        while True:
            # Validação da resposta
            while True:
                try:
                    print('''[1] Adicionar Série
[2] Assistir Série
[3] Atualizar Série
[4] Deletar Série
[0] Menu inicial''')
                    r = int(input())
                    if r < 0 or r > 4:
                        print('Opção inválida!')
                    else:
                        break
                except:
                    print('Digite apenas número!')

            # Condições de acordo com a resposta do menu
            if r == 1:  # Adicionar uma série
                print('Titulo: ')
                titulo = input()
                if titulo == '0':
                    break
                print('Direção: ')
                direcao = input()
                while True:
                    try:
                        print('Ano: ')
                        ano = int(input())
                        break
                    except:
                        print('\nDigite apenas número inteiro!\n')
                print('Genero: ')
                genero = input()
                print('Sinopse: ')
                sinopse = input()
                while True:
                    try:
                        print('Episódios: ')
                        ep = int(input())
                        break
                    except:
                        print('\n Digite apenas número inteiro! \n')
                print('Produtora: ')
                prod = input()
                serie = Serie('visual', id_serie, titulo, direcao,
                              ano, genero, sinopse, ep, prod)
                serie.armazenar(serie)
                id_serie += 1
            elif r == 2:  # Assistir uma série
                print('Qual série deseja assistir?')
                serie.buscaTudo()
                serie.reproduzir(int(input()) - 1)

            elif r == 3:  # Editar uma série
                print('Qual série deseja editar?')
                serie.buscaTudo()
                index = int(input()) - 1
                print(
                    f'O que você deseja editar em {listaSeries[index]["titulo"]}?')
                for i, k in enumerate(listaSeries[index].keys()):
                    if i > 1:
                        print(f'[{i - 1}] {k.capitalize()}')
                key = int(input()) + 1
                key = list(listaSeries[index].keys())[key]
                print(
                    f'Você deseja alterar {key.capitalize()}: {listaSeries[index][key]} para qual valor?')
                valor = input()
                serie.atualizar(index, key, valor)
            elif r == 4:  # Deletar uma série
                print('Qual série deseja deletar?')
                serie.buscaTudo()
                index = int(input()) - 1
                serie.deletar(index)
            else:
                break  # Voltar ao menu inicial
    elif r == 3:
        print(f'{"-" * 10} MÚSICA {"-" * 10}')
        while True:
            print('''[1] Adicionar Música
[2] Reproduzir Música
[3] Atualizar Música
[4] Deletar Música
[0] Menu Principal''')
            while True:
                try:
                    r = int(input('Selecione uma opção: '))
                    if r < 0 or r > 4:
                        print('Valor Inválido!')
                    else:
                        break
                except:
                    print('Digite um número inteiro entre as opções!')
            if r == 1:
                titulo = input('Digite um título: ')
                artista = input('Qual o nome do(a) artista: ')
                ano = input('Qual o ano de lançamento: ')
                album = input('Qual é o nome do album: ')
                genero = input('Qual o genero dessa música: ')
                musica = Musicas('audio', id_musica, artista,
                                 album, ano, genero, titulo)
                musica.armazenar(musica)
                id_musica += 1
            elif r == 2:
                print('Qual Música você quer ouvir? ')
                musica.buscaTudo()
                musica.reproduzir(int(input()) - 1)
            elif r == 3:
                index = int(input('Qual Música você quer atualizar? ')) - 1
                musica.buscaTudo()
                print(
                    f'O que você quer atualizar na música {listaMusica[index]["titulo"]}? ')
                for i, k in enumerate(listaMusica[index].keys()):
                    if i > 1:
                        print(f'[{i-1}][{k.capitalize()}] ')
                key = int(input()) + 1
                key = list(listaMusica[index].keys())[key]
                print(f'Você deseja atualizar a {key.capitalize()}: {listaMusica[index][key]} para qual valor? ')
                valor = input()
                musica.atualizar(index, key, valor)

            elif r == 4:
                print('Qual Música você quer deletar? ')
                musica.buscaTudo()
                musica.deletar(int(input()) - 1)
            else:
                break
    elif r == 4:
        print(f'{"-" * 10} PODCAST {"-" * 10}')
        while True:  # feito um laço de repetição para também proteger o code de quebrar por algum erro do user
            print('''[1] Adicionar um Podcast?
[2] Assistir um Podcast?
[3] Atualizar algum Podcast?
[4] Deletar um Podcast?
[0] Menu Principal''')
            while True:
                try:
                    n = int(input('Digite uma opção: '))
                    if n < 0 or n > 4:
                        print('Opção inválida! ')
                    else:
                        break
                except:
                    print('Digite apenas opções válidas por favor! ')
            if n == 1:  # parte do menu para adicionar um podcast
                print('Qual o título do Podcast?  ')
                titulo = input('Título: ')
                if titulo == 0:
                    break
                print('Host: ')
                host = input('Quem são os(as) anfitriões(ãs) do progama? ')
                print('Episódio: ')
                episodios = input()
                Podcast = Podcast('audio', id_podcast, titulo, host, episodios)
                Podcast.armazenar(Podcast)
                id_podcast += 1
            elif n == 2:  # parte do menu de para assistir um episódio
                print('Qual episódio gostaria de assistir? ')
                for n, x in enumerate(listaPodcasts):
                    print(f'[{n+1}] {listaPodcasts[n]["titulo"]}')
                Podcast.reproduzir(int(input()) - 1)
            elif n == 3:  # parte do menu para edição de alguma chave
                print('Qual Podcast deseja editar? ')
                Podcast.buscaTudo()
                index = int(input()) - 1
                print(
                    f'O que deseja editar em {listaPodcasts[index]["titulo"]} ?')
                for x, k in enumerate(listaPodcasts[index].keys()):
                    if x > 1:
                        print(f'[{x - 1}] {k.capitalize()}')
                key = int(input()) + 1
                key = list(listaPodcasts[index].keys())[key]
                print(
                    f'Você deseja alterar {key.capitalize()}: {listaPodcasts[index][key]} para? ')
                valor = input()
                Podcast.atualizar(index,key,valor)
            elif n == 4:  # deletar um podcast
                print('Qual Podcast deseja deletar? ')
                Podcast.buscaTudo()
                Podcast.deletar(int(input())-1)

            else:
                break  # Menu Principal
    else:
        break  # Finaliza programa
print(f'- Obrigado por usar SoulFlix, até a próxima! :) -')