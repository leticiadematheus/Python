class Produto:
    def __init__(self,descricao, preco, qtd, id):#def é um construtor da classe
        self.__id = id #bolo é self, ele q guarda os ingredientes, mas ainda nao tenho ele pronto __esconde  a veriavel no main (vira privada)
        self.__descricao = descricao
        self.__preco = preco
        self.__qtd = qtd

    #funcao para acessar variavel privada (privada nao pode alterar diretamente) = getter (pegar var e devolve valor, sem alterar a variavel)
    #setter atribui outro valor à variavel, sem ler
    @property
    def descricao(self):
        return self.__descricao
    @property
    def preco(self):
        return self.__preco
    @property
    def qtd(self):
        return self.__qtd
    @property
    def id(self):
        return self.__id

    #funcoes para ler as var privadas
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @preco.setter
    def preco (self, preco):
        self.__preco = preco

    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd

    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        return f'Codigo:  {self.id}\t Descricao:{self.descricao}\tPreco: R${self.preco}\t Qtd : {self.qtd}'