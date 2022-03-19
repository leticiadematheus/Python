#veiculos.py«
#classe filha herda as coisas da mae
#coloca entap na filha so q tem de diferente entre uma filha e outra
#vamos fazer uma estacionamento -> veiculos -> carro, moto, barco

#classe mae é super classe
class Veiculo:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def __str__(self):
        returnn'Veiculo placa:' + self.placa

    def ligar(self):
        print('Veiculo ligado...')

    def abastecer(self):
        print('Veiculo abastecendo...')

#classe filha
class Carro(Veiculo): #carro herda de veiculo
    def __init__(self, marca, modelo, placa, ano,cor):
        super().__init__(marca, modelo, placa, ano)
        self.cor = cor #tem qfazer isso pq na classe mae n tem


    def ligar(self):
        print('Carro ligado')

    def abastecer(self):
        print('Carro abastecendo')

#classe filha
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, placa, ano,cilindrada):
        super().__init__(marca, modelo, placa, ano)
        self.cilindrada = cilindrada #tem qfazer isso pq na classe mae n tem
        

    def ligar(self):
        print('Moto ligado')

    def abastecer(self):
        print('Moto abastecendo')

m = Motocicleta ('Honda', 'CG', 'mmm-1234',2021,600)
m.ligar()
m.abastecer()       
print(m.marca)
        

#v = Veiculo('VW', 'Polo', 'AXX-1234', 2018)
#v.ligar()
#v.abastecer()
#v.marca = 'Fiat' #ele muda pq atributo nao ta privadom o certo é fazer privado
#print(v.marca)

c = Carro('VW', 'Polo', 'AXX-1234', 2018, 'branco')
c.ligar()
c.abastecer()       
print(c.marca)
