#etsrutura de dados (lista,tupla, dicionario,conjunto)

#---> Lista, pode conter elementos duplicados
#contem elemntos em ordem = possui indice (q começa em 0)
lista = ["banana","Laranja","banana","uva","laranja","uva"]
print(lista)
print(lista[5])
if lista[0]=='banana':
    print('tem')
if 'banana' in lista:
    print('tem banana na lista')

#---> List comprehension
entrada =['a',1,'b','c',2,3,'c','d']
saida=[]
[saida.append(x)
 for x in entrada if type (x)  ==int]
print (saida)

for x in entrada:
        if type(x)==int:
            saida.append(x)


#---> Conjunto, retira os elementos duplicados
#não possui indice
conjunto = {"banana","Laranja","banana","uva","laranja","uva"}
#RESULT=conjunto = {'uva', 'banana','laranja'}
print(conjunto)
#print(conjunto[0])#erro nao possui indice
if 'banana' in conjunto:
    print('tem banana no conjunto')

#--->Set comprehension

letras = {x for x in 'abacradabra' if x not in 'abc'}
print (letras)


#--->Dicionário é formado pelo par {}: valor
#é um conjunto q contemchave valor, nao pode ser duplicado e nao tem inidice(mas usa chave como indice)
# se digitar uma chave q nao existe da erro
#chave é o indice do dicionario, portanto não pode ser duplicada
contatos = {'joao': '3028-7898', 'maria':'9999-9998'}
print(contatos['joao'])
print(contatos['maria'])

#altera o conteúdo da chave
contatos['joao'] = '3333-4444'

#retorna lista de chaves
print(list(contatos))
#existe luiz no dicionario?
if 'joao' in contatos:
    print(f'contato do joao encontrado:{contatos["joao"]}')
else:
    print(f'contato do joao não encontrado')


#dicionario criado a partir da lista
lista_contatos=[
    ('Joao','3028-0449'),
    ('Pedro','999-9999'),
    ('Ana','7777-7777'),
    ('Mariana','6666-6666')    
    ]
#converte a lista de tuplas em um dicionario de contatios
dic_contatos=dict(lista_contatos)

#imprime as chaves
print(dic_contatos.keys())

#imprime os valores
print(dic_contatos.values())

for nome in dic_contatos.keys():
    print(f'{nome} = {dic_contatos[nome]}')

#apaga contato
del dic_contatos['Pedro']
if 'Pedro' not in dic_contatos:
    print('nao tem pedro')

          
