#planilha_dataframe.py
#data frame é um obj da biblioteca pandas

import xlsxwriter
import os
import pandas as pd

#cria dicionario usando um data frame para preencher as informações da planilha

dataFrame = pd.DataFrame({'Nome': ['Joao','Veronica','Sabrina','Noemi'],
                          'Idade':[30,25,19,23],
                          'Salario':[3000, 4500, 2900,5500]
                          })

#cria e salva a planilha usando o pandas  pd.ExcelWriter

arquivo = pd.ExcelWriter('quarto_arquivo.xlsx', engine='xlsxwriter')

#Converte o data frame em um objeto do excel
dataFrame.to_excel(arquivo, sheet_name = 'Dados')

#Pega pasta de trabalho xlsxwriter (workbook) e os objetos da planilha
workbook = arquivo.book
worksheet = arquivo.sheets['Dados']

#variavel para colocar formato da moeda
formatoMoeda = workbook.add_format({'num_format': '#,##0.00'})

#Adiciona formato da moeda na coluna
worksheet.set_column('D:D',None,formatoMoeda)

#fecha arquivo
workbook.close()

#abre planilha com excel
os.startfile(arquivo)
