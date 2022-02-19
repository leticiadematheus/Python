#instaola pelo cmd
#pip install pywin32
import random
import win32com.client as win32

def jogar():
    speaker = win32.Dispatch('SAPI.SpVoice')
    speaker.Speak('Bem vindo ao jogo de adivinhação, Leticia')

    print("################################")
    print("bem vindo ao jogo de adivinhação")
    print("################################")

    numero_secreto=random.randrange(1,101)#gera um numero entre 1 e 100
    #print(numero_secreto)

    total_tentativas=10
    pontos = 1000

    print('qual o nivel de dificuldade')
    print('(1)Fácil (2)Médio (3)Difícil')

    nivel=int(input('defina o nivel: '))

    if (nivel==1):
        total_tentativas  =20
    elif (nivel==2):
        total_tentativas  =10
    else:
        total_tentativas  =5

    for tentativa in range(1, total_tentativas+1):
        print(f'Tentativa {tentativa} de {total_tentativas}')    

        #chute = input('Digite um numero entre 1 e 100') #isso retorna string tem q colocar p/ retornar inteiro
        chute = int(input('Digite um numero entre 1 e 100: '))
        if (chute < 1 or chute > 100):
            print('voce deve digitar m numero entre 1 e 100')
            continue

        if chute == numero_secreto:
            print('acertou o numero')
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute) #abs = valor absoluto sem sinal
            pontos = pontos - pontos_perdidos
            if (chute > numero_secreto):
                print ('errou! chute maior q numero secreto')
            else:
                 print ('errou! chute menor q numero secreto')                       
    print('fim jogo')
    print (f' o numrto secreto era {numero_secreto}. Voce fez {pontos} pontos')

#se nao importar, executa
if (__name__=='__main__'):
    jogar()
