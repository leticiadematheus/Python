#pip3 install flask==2.0.3

from flask import Flask, render_template, request, redirect, url_for, flash, session
from produto import Produto #nome da classe sempre maiusculo
from dao import ProdutoDAO
produto_dao = ProdutoDAO('produtos_db.db')

#produto.descricao = "pc intel" #funcão, se fosse a prorpiedade nao tinha parametro ()
#print(produto.informacoes()) #retonar todos os dados sem preicsar de um print p/ cada
#print(produto.descricao)
#print(produto.preco)
#print(produto.qtd)
#print(produto.id)

app = Flask(__name__)
app.secret_key = 'softgraf'

@app.route('/')
def index():
    lista = produto_dao.listar()
    return render_template('relatorio.html', titulo = 'relatorio de estoque', produtos=lista)

@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session ['usuario_logado']== None:
        return redirect(url_for('login'))
    return render_template('cadastrar.html', titulo='Cadastrar novo produto')

@app.route('/salvar', methods=['POST'])
def salvar():
    id = request.form['id']
    descricao = request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']

    produto = Produto(descricao, preco, quantidade, id)
    produto_dao.salvar(produto)
    return redirect(url_for('index'))

@app.route('/editar/<string:id>')
def editar(id):
    produto = produto_dao.buscar_por_id(id)
    return render_template('editar.html', titulo='Editar Produto', produto=produto)

@app.route('/deletar/<string:id>')
def deletar(id):
    produto_dao.deletar(id)
    flash('O produto foi removido com sucesso!')
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['post'])
def autenticar():
    if request.form['senha'] == '123':
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario']+' logou com sucesso')
        return redirect (url_for ('index'))
    else:
        flash('Senha inválida! Tente novamente.')
        return redirect('/login')


    return 'OK'

app.run(debug=True, port=80)