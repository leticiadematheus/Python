#planilha_propriedades.py

import xlsxwriter
import os
import datetime

caminhoArquivo = "terceiro_arquivo.xlsx"

workbook = xlsxwriter.Workbook(caminhoArquivo)

#propriedades da planilha
workbook.set_properties({
    'category':'estudante',
    'title':'Arquivo do excel criado com pyhton',
    'subject':'Aula pythion Excel',
    'author':'Leticia',
    'company':'Makita',
    'create': datetime.date(2022,3,5),
    'comments':'bem vindo ao python para excel'
})

#criar sheet em branco com nome Dados
worksheet = workbook.add_worksheet('Dados')

#armazena a cor amarela para ser usada como cor de fundo na celula
corFundo=workbook.add_format({'fg_color':'yellow'})

#aramzena cor azul para ser usada como cor da fonte
corFonte=workbook.add_format()
corFonte.set_font_color('blue')


#adiciona dados no worksheet
worksheet.write('A1','Nome', corFundo)
worksheet.write('B1','Idade', corFundo)
worksheet.write('A2','Joao da Silva')
worksheet.write('B2',33, corFonte)
worksheet.write('A3','Maria da Silva')
worksheet.write('B3',32, corFonte)

#fecha arquivo
workbook.close()

#abre planilha
os.startfile(caminhoArquivo)
