#primeira_planilha.py
#https://xlsxwriter.readthedocs.ic

#pip install xlsxwriter

import xlsxwriter
import os

caminhoArquivo = "primeiro_arquivo.xlsx"

workbook = xlsxwriter.Workbook(caminhoArquivo)

#criar sheet em branco com nome Sheet1
worksheet = workbook.add_worksheet()

#adiciona dados no worksheet
worksheet.write('A1','Nome')
worksheet.write('B1','Idade')
worksheet.write('A2','Joao da Silva')
worksheet.write('B2','33')
worksheet.write('A3','Maria da Silva')
worksheet.write('B3','32')

#fecha arquivo
workbook.close()

#abre planilha
os.startfile(caminhoArquivo)
