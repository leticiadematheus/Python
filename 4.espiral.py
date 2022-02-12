#espiral

import turtle
"""
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# ate aqui era um

# cored red yellow green orange purple
turtle.pencolor("red")
turtle.bgcolor ("black")
for x in range (50):
    #turtle.forward(x * 5)
    turtle.circle(x * 5)    
    turtle.left(91)

    """

cores = ['red', 'yellow', 'blue','green', 'orange', 'purple', 'white', 'brown', 'grey', 'pink']

turtle.bgcolor ("black")
turtle.speed(speed = 500)

def linhas():

    lados = turtle.numinput('escolha entre  2 e 6 ', 'numero de lados: ')

    for x in range (50):
        indice = x % 6 # 0.5
        turtle.pencolor(cores[indice])
        turtle.forward(x * 5)    
        turtle.left(360/(lados+1))
        turtle.width(x*lados/10)

def roseta():
    numero = int(turtle.numinput('Numero de circulos ', 'Quantos circulos vc quer?  ', 6))
    t = turtle.Pen()
    t.speed(1500)
    t.pencolor('yellow')
    for x in range(numero):
        t.circle(200)
        t.left(360/numero)

    t.pencolor('pink')
    for x in range(numero):
        t.circle(300)
        t.left(360/numero)

def animais():
    t = turtle.Pen()
    animais = []
    nome = turtle.textinput('nomes de animais', 'digite um nome ou enter para terminar: ')

    #continua pedindo nomes
    while nome != "" and len(animais)< len(cores) :
        #adiciona o nome à lista de animais
        animais.append(nome.title())
        #pede outro nome ou termina
        nome = turtle.textinput('nomes de animais', 'digite um nome ou enter para terminar: ')
        #desenha espiral com os nomes dos animais

    for x in range (100):
        t.pencolor(cores[x % len(animais)])
#circula pelas cores
        t.penup() #nao desenha as linhas normais da espiral
        t.forward(x*4)#move a tarturuga sem desenhar
        t.pendown()#desenha nome do proximo animal
        t.write(animais[x%len(animais)], font = ('Arial', int((x+4)/4), "bold"))
        t.left(360/len(animais) +2)
        
if(__name__=='__main__'):#começa por aqui e executa a função roseta
    animais()




