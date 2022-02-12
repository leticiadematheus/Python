#calc exp
expressao = input('digite uma expressao:')
print (expressao)
lista = expressao.split('+')
print(lista)
soma = 0
for x in lista:
    soma = soma + int(x)
print('soma', soma)


              
