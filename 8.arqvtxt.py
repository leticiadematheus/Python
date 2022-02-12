#arqv txt

import sys

#modo de abertura de arqv
# r = somente leitura
# w = write
# a = anexar
lista = []

def entrada ():
    fruta = input('Nome da fruta para add:')
    lista.append(fruta)
    print(fruta + '\n adicionada')
def mostrar():
    print('lista = ', lista)
def gravar():
    arquivo = open('frutas.txt','w')
    for fruta in lista:
        arquivo.write(fruta+'\n')
    arquivo.close()
    print('daod sgravados')
def ler ():
    pass
def anexar():
    pass
def menu():
    print('#######################')
    print('# Controle de listas  #')
    print('# 1= entrada de dados #')
    print('# 2= mostrar dados    #')
    print('# 3= gravar dados     #')
    print('# 4= ler dados        #')
    print('# 5= anexar dados     #')
    print('#######################')
    opcao = int(input('qual opção?'))

    if (opcao ==1):
        entrada()
    elif (opcao ==2):
        mostrar()
    elif (opcao ==3):
        gravar()
    elif (opcao ==4):
        ler()
    elif (opcao ==5):
        anexar()
    else:
        print('opção invalida')
        

if(__name__=='__main__'):
    while True: #loop infinito
        menu()
    
