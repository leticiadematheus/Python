#matriz np

#para instalar um pct/modulo/biblioteca
#entrar  no cmd
#cd C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\Scripts
#pip install numpy
#numpy é o nome da bib

import numpy as np

print ('Matriz usando numpy')
matriz = np.array([
                [1,2,5,6],
                [3,4,8,9],
                [1,2,5,6],
                [3,4,8,9]
                ])
print(matriz)
print('Matriz[3,3]=', matriz[3][3])

