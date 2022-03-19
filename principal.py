#principal.py

from veiculos import * # se executar sem issonao acha motocicleta pq n ta definido nesse arqv

def principal():

    veiculo = Veiculo('Marca','modelo','placa',1)
    carro = Carro('VW','Polo','ACS-123',2020,'Branco')
    moto = Motocicleta ('Honda', 'CG', 'mmm-1234',2021,600)
    
    veiculo.abastecer()       
    print(veiculo)#chama str automaticamente

    lista = [veiculo,carro,moto,'banana',113,4.2]

    for item in  lista:
        if(isinstance (item, Carro)):
            print('é um carro')
        elif(isinstance (item, Motocicleta)):
            print('é uma motocicleta')
        elif(isinstance (item, Veiculo)):
            print('é um veiculo')
        elif(isinstance (item, str)):
            print('é uma string na lista')
        elif(isinstance (item, int)):
            print('é um int na lista')
        else:
            print('desconhecido')
        
if __name__=='__main__':
        principal()
