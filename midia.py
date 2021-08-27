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


class Filme(Midia):   # CLASSE FILHA DE MIDIA
    def __init__(self,tipo,id,titulo,direcao,ano,genero,sinopse): 
        super().__init__(tipo,id)
        self.titulo = titulo
        self.direcao = direcao
        self.ano = ano
        self.genero = genero
        self.sinopse = sinopse

    
    def armazenar(self,object):  #METHOD ARMAZENAMOS O O FILME DESEJADO A LISTA
        listaFilmes.append(vars(object))
    
  
    def assistir(self, index): # AQUI ESCOLHEMOS O FILME DESEJADO E ASSISTIMOS
        print(f'Você está assistindo o filme {listaFilmes[index]["titulo"]}...')
        sleep(5)

    
    def atualizar(self, index, key, value):  # AQUI SE ALTERA FILMES JÁ ADICIONADOS E ATUALIZA
        listaFilmes[index][key]= value


    def deletar(self,index): #METHOD PARA DELETAR FILMES DA LISTA
        listaFilmes.pop(index)


    def buscaTudo(self):
        for i, f in enumerate(listaFilmes):
            print(f'[{i+1}] {listaFilmes[i]["titulo"]}') # MOSTRA OS FILMES DA LISTA


listaFilmes=[]

id= 0

while True:
    print('''[1] Adicionar Filme
    [2] Assistir Filme
    [3] Atualizar Filme
    [4] Deletar Filme
    [0] Sair do Programa''')


    a = int(input())
    if a == 1:  #MENU PARA ADICIONAR FILME
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
        filme = Filme('visual', id, titulo, direcao, ano, genero, sinopse)
        filme.armazenar(filme)
        id =+ 1
    elif a == 2:  #MENU PARA ESCOLHER E ASSISTIR O FILME
        print('Qual filme deseja assistir?')
        filme.buscaTudo()
        index= int(input())
        filme.assistir(index-1)


    elif a == 3:  #MENU PARA ALTERAR FILMES JÁ ADICIONADOS
        print('Qual filme deseja atualizar?')
        filme.buscaTudo()
        index = int(input())-1
        print(f'O que você deseja editar em {listaFilmes[index]["titulo"]}')
        for i, k in enumerate(listaFilmes[index].keys()):
            if i > 1 :
                print(f'[{i-1}] {k.capitalize()}')
        key= int(input())+1
        key= list(listaFilmes[index].keys())[key]
        print(f'Você deseja alterar {key.capitalize()}: {listaFilmes[index][key]} para qual valor?')
        value = input()
        filme.atualizar(index, key, value)


    elif a == 4:
        print('Qual filme deseja excluir?')
        filme.buscaTudo()
        filme.deletar(int(input())-1)

    
    else:
        break
    print('FIM')
