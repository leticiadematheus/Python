class Conta:

    #propriedades: limite, titular, saldo...
    #funções builtin: __xxx__

    def __init__(self, numero, titular, saldo, limite):
        print("inicializando obj: {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo# underline protege, nao acessa
        self.__limite = limite        

        #métodos
    def depositar(self, valor):
        self.__saldo += valor # saldp = saldo + valor

    def sacar (self, valor):
        if self.__saldo + self.__limite >= valor:
            self.__saldo -= valor
        else:
            print('Nao ha saldo para sacar')
            False

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)
    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite (self, limite):
        self.__limite = limite
        
    @staticmethod #compartilhado entre todos os objetos
    def codigo_banco ():
        return "001"

    @staticmethod
    def codigos_bancos():
        return{'BB':'001','Caixa':'104', 'Bradesco':'237'}

contaJoao = Conta(123,'Joao da Silva',1000000,50)
contaZe = Conta(456,'Jose da Silva',0,300)
print('saldo do ze:', contaZe.saldo)

contaJoao.transferir(50,contaZe)
contaZe.Limite = 200

print('codg do banco: ', Conta.codigo_banco())
print('cdg caixa', Conta.codigos_bancos()['Caixa'])

print('saldo do ze:', contaZe.saldo)
print('titular:', contaZe.titular)
print('limite:', contaZe.limite)



#contaZe.saldo = 1000

#print(contaJoao.saldo)
#contaJoao.depositar(300)
#contaJoao.sacar(5000)
    
