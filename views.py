from flask import render_template, request, redirect, flash, session
from index import app, db
from models import Jogos


banco_usuario={'rafael', 'brunno'}
banco_senha={
    'rafael': 'pantera',
    'brunno' : 'doisdois'}


@app.route('/')
def index ():
    result = Jogos.query.all()
    titulo= 'Jogos Que Já fiz Review!'
    return render_template('lista.html', titulo=titulo, jogos=result )


#adicionando jogo 
@app.route('/newgame')
def newgame ():
    if 'usuario_login' not in session or session['usuario_login'] == None:
        return redirect('/login')
    titulo = 'Jogo'
    return render_template('newgame.html', titulo=titulo )

@app.route('/new', methods = ['POST'])
def new ():
    nome = request.form['nome']
    genero = request.form['genero']
    console = request.form['console']
    jogo = Jogos(nome=nome, genero=genero, console=console)
    db.session.add(jogo)
    db.session.commit()
    return redirect('/')



#EDITANDO JOGO
@app.route('/edit/<int:id>')
def edit (id):
    if 'usuario_login' not in session or session['usuario_login'] == None:
        return redirect('/login')
    jogo= Jogos.query.filter_by(id=id).first()
    return render_template('edit.html', titulo='Editando Jogo ', jogo=jogo )

@app.route('/atualizar', methods=['POST',])
def atualizar ():
    jogo= Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome = request.form['nome']
    jogo.genero = request.form['genero']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    return redirect('/')

@app.route('/deletar/<int:id>')
def deletar (id):
    if 'usuario_login' not in session or session['usuario_login'] == None:
        return redirect('/login')
    
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo foi deletado')
    return redirect('/')
    


#Fazendo login
@app.route('/login')
def login ():
    if session['usuario_login'] != None:
        return redirect('/newgame')
    return render_template('login.html')

@app.route('/autenticador', methods=['POST'])
def autenticador ():
    usuario = request.form['usuario']
    usuario_login = usuario.lower()
    if usuario_login in banco_usuario:
        if banco_senha[usuario_login] == request.form["senha"]:
                session['usuario_login'] = usuario_login
                return redirect('/newgame')
        else:
            flash('Senha incorreta')
            return redirect('/login')
    else:
        flash('Usuario incorreto')
        return redirect('/login')
    

@app.route('/logout')
def logout ():
    flash('Usuario deslogado')
    session['usuario_login'] = None
    return redirect('/login')


#Cadastrando novo usuario 
@app.route('/cadastro')
def cadastro ():
    return render_template('cadastro.html')

@app.route('/novousuario', methods=['POST'])
def novousuario ():
    usuario = request.form['usuario']
    senha = request.form["senha"]
    senha1 = request.form["senha1"]
    usuario_login = usuario.lower()
    if senha == senha1:
        banco_usuario.add(usuario_login)
        banco_senha[usuario_login] = senha
        return redirect('/login')
    else:
        flash('As senhas são diferente')
        return redirect('/cadastro')