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

    
class Musicas(Midia):
    '''Classe para seleção de musicas '''
    def __init__(self, tipo, id, artista, album, ano, genero, titulo): # Método construtor da classe
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

    def buscaTudo(self): # metodo para listar todas as músicas
        for i, m in enumerate(listaMusica):
            print(f'[{i+1}] {listaMusica[i]["titulo"]}')

    def tocar(self, index):
        print(f'Tocando faixa 1 do artista {listaMusica[index]["titulo"]}')
        
        
listaMusica = []
id = 0
while True:
    print('''[1] Adicinor Música
[2] tocar Música
[3] Atualizar Música
[4] Deletar Música
[0] Sair do programa''')
    while True:
        try:
            r = int(input('selecione uma opção: '))
            if r < 0 or r > 4:
                print('Valor Invalido!')
            else:
                break
        except:
            print('Digite um número inteiro entre as opções!')
    if r == 1:
        titulo = input('Digite um titulo: ')
        artista = input('Qual o nome do(a) artista: ')
        ano = input('Qual o ano de lançamento: ')
        album = input('Qual é o nome do album: ')
        genero = input('Qual o genero dessa música: ')
        musica = Musicas('audio', id, artista, album, ano, genero, titulo)
        musica.armazenar(musica)
        id += 1
    elif r == 2:
        print('Qual Música você quer ouvir? ')
        musica.buscaTudo()
        musica.tocar(int(input()) - 1)
    elif r == 3:
        musica.buscaTudo()
        index = int(input('Qual Música você quer atualizar? ')) -1
        print(f'O que você quer atualizar na música {listaMusica[index]["titulo"]}? ')
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
