Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> frutas = []
>>> frutas.append('banana')
>>> frutas.append('laranja')
>>> frutas.append('uva')
>>> frutas
['banana', 'laranja', 'uva']
>>> len(frutas)
3
>>> frutas[0]
'banana'
>>> frutas[0]
'banana'
>>> frutas[1]
'laranja'
>>> frutas[2]
'uva'
>>> carros=['bmw','polo','bravo','fusca','ferrari','lanborgini','corcel']
>>> carros[4]
'ferrari'
>>> carros.index('ferrari')
4
>>> carros[0:7]
['bmw', 'polo', 'bravo', 'fusca', 'ferrari', 'lanborgini', 'corcel']
>>> carros[0:6]
['bmw', 'polo', 'bravo', 'fusca', 'ferrari', 'lanborgini']
>>> carros[0:4]
['bmw', 'polo', 'bravo', 'fusca']
>>> carros[:4]
['bmw', 'polo', 'bravo', 'fusca']
>>> carros[2:4]
['bravo', 'fusca']
>>> carros[2:]
['bravo', 'fusca', 'ferrari', 'lanborgini', 'corcel']
>>> carros[:]
['bmw', 'polo', 'bravo', 'fusca', 'ferrari', 'lanborgini', 'corcel']
>>> carros
['bmw', 'polo', 'bravo', 'fusca', 'ferrari', 'lanborgini', 'corcel']
>>> carros[0:7:2]
['bmw', 'bravo', 'ferrari', 'corcel']
>>> carros[:7:2]
['bmw', 'bravo', 'ferrari', 'corcel']
>>> carros[::3]
['bmw', 'fusca', 'corcel']
>>> carros[::4]
['bmw', 'ferrari']
>>> carros[-1]
'corcel'
>>> carros[-2]
'lanborgini'
>>> carros[-3]
'ferrari'
>>> carros[-6]
'polo'
>>> carros[-7]
'bmw'
>>> carros[-1:-7]
[]
>>> carros[-1:-3]
[]
>>> carros[-5]
'bravo'
>>> carros[6]
'corcel'
>>> carros[6]='palio'
>>> carros
['bmw', 'polo', 'bravo', 'fusca', 'ferrari', 'lanborgini', 'palio']
>>> fruttas.sort()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    fruttas.sort()
NameError: name 'fruttas' is not defined
>>> carros.sort()
>>> carros
['bmw', 'bravo', 'ferrari', 'fusca', 'lanborgini', 'palio', 'polo']
>>> carros.reverse()
>>> carros
['polo', 'palio', 'lanborgini', 'fusca', 'ferrari', 'bravo', 'bmw']
>>> carro='fusca'
>>> carro in carros
True
>>> 'fusca' in carros
True
>>> 'peugeot' in carros
False
>>> "pegeot"in carros
False
>>> "peugeot" not in carros
True
>>> carros
['polo', 'palio', 'lanborgini', 'fusca', 'ferrari', 'bravo', 'bmw']
>>> prints(carros)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    prints(carros)
NameError: name 'prints' is not defined
>>> print(carros)
['polo', 'palio', 'lanborgini', 'fusca', 'ferrari', 'bravo', 'bmw']
>>> for x in carros:
	print(x)

	
polo
palio
lanborgini
fusca
ferrari
bravo
bmw
>>> for carro in carros:
	print(x)

	
bmw
bmw
bmw
bmw
bmw
bmw
bmw
>>> for carro in carros:
	print(carro)

	
polo
palio
lanborgini
fusca
ferrari
bravo
bmw
>>> lista=[0,1,2,3,4,5,6,7,8,9]
>>> for x in lista
SyntaxError: invalid syntax
>>> print(x)
bmw
>>> for x in lista:
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> range(10)
range(0, 10)
>>> range(10)
range(0, 10)
>>> for x in range(10):
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista[5]='banana'
>>> lista
[0, 1, 2, 3, 4, 'banana', 6, 7, 8, 9]
>>> lista=[0,1,2['banana','uva','laranja'],[5,7],['bmw','fusca','corcel'],['bom', 'dia']
       lista[0]
       
SyntaxError: invalid syntax
>>> lista[1]
1
>>> lista[2]
2
>>> lista[3]
3
>>> lista=[0,1,2,['banana','uva','laranja'],[5,7],['bmw','fusca','corcel'],'bom', 'dia']









       lista[0]
KeyboardInterrupt
>>> lista=[0,1,2,['banana','uva','laranja'],[5,7],['bmw','fusca','corcel'],'bom', 'dia']
>>> lista[1]
1
>>> lista[2]
2
>>> lista[3]
['banana', 'uva', 'laranja']
>>> lista[3][0]
'banana'
>>> lista[5][1]
'fusca'
>>> tupla = (0,1,2,3,4,5)
>>> tupla[2]
2
>>> tupla[2]=123
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    tupla[2]=123
TypeError: 'tuple' object does not support item assignment
>>> lista
[0, 1, 2, ['banana', 'uva', 'laranja'], [5, 7], ['bmw', 'fusca', 'corcel'], 'bom', 'dia']
>>> tuple(lista)
(0, 1, 2, ['banana', 'uva', 'laranja'], [5, 7], ['bmw', 'fusca', 'corcel'], 'bom', 'dia')
>>> valores = 91.0,5.5,8.9)
SyntaxError: unmatched ')'
>>> valores = (1.0,5.5,8.9)
>>> valores[0]
1.0
>>> valores[0]=11
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    valores[0]=11
TypeError: 'tuple' object does not support item assignment
>>> valores.sort()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    valores.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> valores.reverse()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    valores.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> valores.append(9)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    valores.append(9)
AttributeError: 'tuple' object has no attribute 'append'
>>> valores
(1.0, 5.5, 8.9)
>>> for x in valores:
	print(x)

	
1.0
5.5
8.9
>>> for x in valores:
	print('RS %d'%x)

	
RS 1
RS 5
RS 8
>>> for x in valores:
	print('RS %.2f'%x)

	
RS 1.00
RS 5.50
RS 8.90
>>> print('valor: %.5f' %3.1415926)
valor: 3.14159
>>> nome = input ('digite seu nome')
digite seu nomeleticia
>>> 
>>> nome
'leticia'
>>> valor = input('digite um valor:')
digite um valor:55
>>> valor
'55'
>>> valor + 1
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    valor + 1
TypeError: can only concatenate str (not "int") to str
>>> valor = int(inout('digite valor: '))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    valor = int(inout('digite valor: '))
NameError: name 'inout' is not defined
>>> valor = int(input('digite um valor:'))
digite um valor:55
>>> valor+1
56
>>> valor = int(input('digite um valor:'))
digite um valor:3.14
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    valor = int(input('digite um valor:'))
ValueError: invalid literal for int() with base 10: '3.14'
>>> valor = float(input('digite um valor:'))
digite um valor:3.14
>>> valor+1
4.140000000000001
>>> limite = int(input('digite uim int : '))
digite uim int : 100
>>> for x in range(limite):
	print(x)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> for x in range (0,360) int x
SyntaxError: invalid syntax
>>> for x in range (0,360):
	print(x)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
>>> for x in range(0,360,45):
	print(x)

	
0
45
90
135
180
225
270
315
>>> a = eval(input('digite um valor: '))
digite um valor: 10
>>> a = eval(input('digite um valor: '))
digite um valor: 3.14
>>> a
3.14
>>> #comentario
>>> 
============================================================================================ RESTART: E:/Curso python - Leticia/1.Calculadora.py ===========================================================================================
>>> 
============================================================================================ RESTART: E:/Curso python - Leticia/1.Calculadora.py ===========================================================================================
valor total=  3.0
>>> 
============================================================================================ RESTART: E:/Curso python - Leticia/1.Calculadora.py ===========================================================================================
valor total=  2.5
>>> 
============================================================================================================== RESTART: Shell ==============================================================================================================
>>> 
=============================================================================================== RESTART: E:/Curso python - Leticia/2.Frase.py ==============================================================================================
digite uma frase:oi
oi
>>> frase = 'o rato roeu a roupa do rei de roma'
>>> frase.split()
['o', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'roma']
>>> frase.split()[0]
'o'
>>> frase.split()[1]
'rato'
>>> frase.split()[2]
'roeu'
>>> frase.split()[3]
'a'
>>> frase.split()[4]
'roupa'
>>> frase.split('')
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    frase.split('')
ValueError: empty separator
>>> frase.split('r')
['o ', 'ato ', 'oeu a ', 'oupa do ', 'ei de ', 'oma']
>>> expressao = '10+5+8+3'
>>> expressao.split('+')
['10', '5', '8', '3']
>>> 
=============================================================================================== RESTART: E:/Curso python - Leticia/2.Frase.py ==============================================================================================
digite uma expressao:10+5+8+7+3
10+5+8+7+3
['10', '5', '8', '7', '3']
>>> 
=============================================================================================== RESTART: E:/Curso python - Leticia/2.Frase.py ==============================================================================================
digite uma expressao:10+5+8+7+3
10+5+8+7+3
['10', '5', '8', '7', '3']
soma 33
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
u
m
 
p
e
q
u
e
n
o
 
p
a
s
s
o
 
p
a
r
a
 
o
 
p
y
t
h
i
n
 
p
o
r
e
m
 
u
m
 
g
r
a
n
d
e
 
p
a
s
s
o
 
p
a
r
a
 
a
 
h
u
m
a
n
i
d
a
d
e
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/3.tabela ascii.py", line 4, in <module>
    print(letra, ens = '')
TypeError: 'ens' is an invalid keyword argument for print()
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
um pequeno passo para o pythin porem um grande passo para a humanidade
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
u m   p e q u e n o   p a s s o   p a r a   o   p y t h i n   p o r e m   u m   g r a n d e   p a s s o   p a r a   a   h u m a n i d a d e 
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
u m   p e q u e n o   p a s s o   p a r a   o   p y t h i n   p o r e m   u m   g r a n d e   p a s s o   p a r a   a   h u m a n i d a d e 
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
u m   p e q u e n o   p a s s o   p a r a   o   p y t h i n   p o r e m   u m   g r a n d e   p a s s o   p a r a   a   h u m a n i d a d e 9
8
7
6
5
4
3
2
1
>>> chr(65)
'A'
>>> chr(66)
'B'
>>> chr(67)
'C'
>>> chr(68)
'D'
>>> chr(48)
'0'
>>> chr(49)
'1'
>>> chr(50)
'2'
>>> chr(10)
'\n'
>>> chr(13)
'\r'
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
ABCDEFGHIJKLMNOPQRSTUVWXYZ
>>> ord('a')
97
>>> ord('A')
65
>>> ord('0')
48
>>> 
=========================================================================================== RESTART: E:/Curso python - Leticia/3.tabela ascii.py ===========================================================================================
ABCDEFGHIJKLMNOPQRSTUVWXYZ
 digite uma palavra:oi
senha: 111105
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3177, in _goto
    screen._drawline(self.drawingLineItem,
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 546, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 2762, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 17, in <module>
    turtle.forward(x * 5)
  File "<string>", line 12, in forward
turtle.Terminator
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 18, in <module>
    turtle.circle(x * 5)
  File "<string>", line 8, in circle
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1991, in circle
    self.speed(speed)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2175, in speed
    self.pen(speed=speed)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2460, in pen
    self._update()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 4%2
0
>>> 3%2
1
>>> 2%2
0
>>> 1%2
1
>>> 100 % 6
4
>>> 99 % 6
3
>>> 98 % 6
2
>>> 97 % 6
1
>>> 96 % 6
0
>>> 94 % 6
4
>>> # % resto
>>> 94%9
4
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 30, in <module>
    turtle.pencolor(cores[indice])
IndexError: list index out of range
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 31, in <module>
    turtle.circle(x * 5)
  File "<string>", line 8, in circle
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1991, in circle
    self.speed(speed)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2175, in speed
    self.pen(speed=speed)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2460, in pen
    self._update()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 49, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 43, in roseta
    t.pencolor('yellow')
AttributeError: 'dict' object has no attribute 'pencolor'
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 49, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 43, in roseta
    t.pencolor('yellow')
AttributeError: 'dict' object has no attribute 'pencolor'
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 49, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 45, in roseta
    t.circle(100)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1992, in circle
    self._go(l)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 756, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 2762, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 50, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 45, in roseta
    for x in range(numero):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 50, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 46, in roseta
    t.circle(100)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1992, in circle
    self._go(l)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 756, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 2762, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 51, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 47, in roseta
    t.circle(100)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1991, in circle
    self.speed(speed)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2175, in speed
    self.pen(speed=speed)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2460, in pen
    self._update()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 51, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 47, in roseta
    t.circle(100)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1991, in circle
    self.speed(speed)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2175, in speed
    self.pen(speed=speed)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2460, in pen
    self._update()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 51, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 43, in roseta
    t.speed(speed = 1500)
UnboundLocalError: local variable 't' referenced before assignment
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 51, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 43, in roseta
    t.speed(1500)
UnboundLocalError: local variable 't' referenced before assignment
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 56, in <module>
    roseta()
  File "E:/Curso python - Leticia/4.espiral.py", line 47, in roseta
    t.circle(1000)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1992, in circle
    self._go(l)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 756, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 2762, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 77, in <module>
    animais()
NameError: name 'animais' is not defined
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 77, in <module>
    animais()
  File "E:/Curso python - Leticia/4.espiral.py", line 68, in animais
    t.pencolor(cores[x % len(animais)])
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2258, in pencolor
    return self._color(self._pencolor)
AttributeError: 'str' object has no attribute '_color'
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 77, in <module>
    animais()
  File "E:/Curso python - Leticia/4.espiral.py", line 73, in animais
    t.write(animals[x%len(animais)], font = ('Arial', int((x+4)/4), "bold"))
NameError: name 'animals' is not defined
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 77, in <module>
    animais()
  File "E:/Curso python - Leticia/4.espiral.py", line 74, in animais
    t.left(360/len(animais) +2)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1700, in left
    self._rotate(angle)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3277, in _rotate
    self._update()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
Traceback (most recent call last):
  File "E:/Curso python - Leticia/4.espiral.py", line 77, in <module>
    animais()
  File "E:/Curso python - Leticia/4.espiral.py", line 74, in animais
    t.left(360/len(animais) +2)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1700, in left
    self._rotate(angle)
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3277, in _rotate
    self._update()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\ALUNO-402\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
============================================================================================== RESTART: E:/Curso python - Leticia/4.espiral.py =============================================================================================
>>> "macaco".title()
'Macaco'
>>> 1+2
3
]
>>> 1-3
-2
>>> 2/8
0.25
>>> 4*9
36
>>> 4//3
1
>>> 4/3
1.3333333333333333
>>> 9//2
4
>>> 9%2
1
>>> 2**3]
SyntaxError: unmatched ']'
>>> 2**3
8
>>> math.pow(2,3)
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    math.pow(2,3)
NameError: name 'math' is not defined
>>> import math
>>> math.pow(2,3)
8.0
>>> math.sqrt(9)
3.0
>>> 4 == 4
True
>>> 4!=5
True
>>> 5<4
False
>>> 4>5
False
>>> 5>=4
True
>>> 4<=5
True
>>> "uva" != "banana"
True
>>> "4" != "6"
True
>>> #texto formatado
>>> print("\n %s = %.2f\n%s = %d kg" % ("preço banana " , 1.99, "Quantidade", 3))

 preço banana  = 1.99
Quantidade = 3 kg
>>> 