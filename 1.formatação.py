#formatação
valor1=10
valor2=20.9

#primeira forma de formatação usando %
print("V1= %d V2 = R$ %.2f " % (valor1, valor2))

#segunda  unsando {}
print("v1= R$ {} v2 = R$ {:.2f}".format(valor1,valor2))

print("Olá Sr.{0}{1}".format("joao", "ferreira"))
print("Sobrenome:{1}\tNome: {0}".format("joao", "ferreira"))

print("R${:6.1f}".format(1000.12))#total 6 casas, sendo 1 decimal , preenche as anteriores com espaços em branco
print("R${:07.2f}".format(4.11))#total 7 casas, sendo 2 decimais 

#terceira forma de formatação: f-string
#função incluída a partir da versão 3.6 do python

nome = "Matheus"
print(f'Meu nome é {nome}')

print(f'Meu nome é {nome.lower()}')
