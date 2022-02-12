Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista=[1,2,3,[4,5,6,[7,8,9]]]
>>> lista[1]
2
>>> lista[2]
3
>>> lista[4]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lista[4]
IndexError: list index out of range
>>> lista[3][0]
4
>>> lista[3][1]
5
>>> lista[3][2]
6
>>> lista[3][3]
[7, 8, 9]
>>> lista[3][3][0]
7
>>> lista[3][3][1]
8
>>> lista[3][3][2]
9
>>> lista[3][3][3]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    lista[3][3][3]
IndexError: list index out of range
>>> 
Warning (from warnings module):
  File "E:/Curso python - Leticia/Aula1/5.matriz.py", line 5
    [1,2,5,6]
SyntaxWarning: list indices must be integers or slices, not tuple; perhaps you missed a comma?
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/Aula1/5.matriz.py ===========================================================================================
matriz usando lista...
Traceback (most recent call last):
  File "E:/Curso python - Leticia/Aula1/5.matriz.py", line 5, in <module>
    [1,2,5,6]
TypeError: list indices must be integers or slices, not tuple
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/Aula1/5.matriz.py ===========================================================================================
matriz usando lista...
[[1, 2, 5, 6], [3, 4, 8, 9], [3, 4, 8, 9], [1, 2, 5, 6]]
1
6
[1, 2, 5, 6]
[3, 4, 8, 9]
[3, 4, 8, 9]
[1, 2, 5, 6]
>>> 0*10
0
>>> [0]*10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> [123]*100
[123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123]
]
>>> ['BANANA']*100
['BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA', 'BANANA']
>>> linha = [0] * 4
>>> 
>>> linha
[0, 0, 0, 0]
>>> linha*3
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> linha *10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> matriz = [linha]*4
>>> matriz
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/Aula1/5.matriz.py ===========================================================================================
matriz usando lista...
[[1, 2, 5, 6], [3, 4, 8, 9], [3, 4, 8, 9], [1, 2, 5, 6]]
1
6
[1, 2, 5, 6]
[3, 4, 8, 9]
[3, 4, 8, 9]
[1, 2, 5, 6]

 qtd de linhas:5

 qtd de colunas 3
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
>>> 