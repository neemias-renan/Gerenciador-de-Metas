from flask import render_template,request,redirect,url_for
from flask_login import login_user,logout_user,current_user,login_required
from app import app, db, lm

from app.models.tables import User, Meta

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id = id).first()

@app.route("/login", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
@app.route("/", methods=['GET','POST'])
def login():
    alerta_erro = ''
    if request.method == 'POST':
        email_input = request.form['email']
        senha_input = request.form['senha']
        user = User.query.filter_by(email = email_input).first()

        if user and user.senha == senha_input:
            login_user(user)
            return redirect(url_for('metas'))
        else:
            alerta_erro = "Dados Incorretos"
    return render_template('index.html',alerta_erro = alerta_erro)

@app.route("/registrar_user", methods=['GET', 'POST'])
def registrar_user():
    alerta_erro = ''
    try:
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            confirmar_senha = request.form['confirmar_senha']

            if nome == '' or email == '':
                alerta_erro = 'Adicione todos os dados'
            else:
                if senha == confirmar_senha:
                    user = User(nome,email,senha)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('login'))
                else:
                    alerta_erro = 'As senhas não são as mesmas.'
    except:
        alerta_erro = 'Esse email já está em uso.'
    return render_template('registrar_user.html', alerta_erro = alerta_erro)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/metas")
@login_required
def metas():
    meta = ''
    user_id_input = current_user.id

    metas_user = Meta.query.filter_by(user_id = user_id_input).all()
    meta = metas_user
    quantidade_metas = len(metas_user)
    return render_template('metas.html',meta = meta, quantidade_metas = quantidade_metas)

@app.route("/configuracao", methods=['GET','POST'])
@login_required
def configuracao():
    variavel1 = current_user.nome
    variavel2 = variavel1.split(" ")
    nome = variavel2[0]
    dados = current_user
    alerta_erro = ''
    if request.method == 'POST':
        NovoNome = request.form['novoNome']
        NovoEmail = request.form['novoEmail']
        NovaSenha = request.form['novaSenha']
        confirmarSenha = request.form['confirmarnovaSenha']


        if NovoNome == '' or NovoEmail == '':
            alerta_erro = 'Adicione todos os dados'
        
        elif NovaSenha == '' and confirmarSenha == '':
            user = User.query.filter_by(id = dados.id).first()
            user.nome = NovoNome
            user.email = NovoEmail
            db.session.commit()
            return redirect(url_for('metas'))

        else:
            if NovaSenha == confirmarSenha:
                user = User.query.filter_by(id = dados.id).first()
                user.nome = NovoNome
                user.email = NovoEmail
                user.senha = NovaSenha
                db.session.commit()
                return redirect(url_for('metas'))
            else:
                alerta_erro = 'As senhas não são as mesmas.'

    return render_template('configuracao.html',nome =nome,dados = dados,alerta_erro= alerta_erro)

@app.route("/adicionar_metas",methods=['GET','POST'])
@login_required
def adicionar_metas():
    alerta_erro=''
    if request.method == 'POST':
        titulo_input = request.form['titulo']
        descricao_input = request.form['descricao']
        user_id_input = current_user.id

        if titulo_input == '' or descricao_input == '':
            alerta_erro = 'Adicione todos os dados'
        else:
            meta = Meta(titulo_input,descricao_input,user_id_input)
            db.session.add(meta)
            db.session.commit()
            return redirect(url_for('metas'))
    return render_template('adicionar_metas.html',alerta_erro =alerta_erro)

@app.route("/editar_metas/<idmeta>",methods=['GET','POST'])
@login_required
def editar_metas(idmeta):    
    atualizar_meta = Meta.query.filter_by(id = idmeta).first()
    if request.method == 'POST':
        titulo_input = request.form['titulo']
        descricao_input = request.form['descricao']

        if titulo_input == '' or descricao_input == '':
            alerta_erro = 'Adicione todos os dados'
        else:
            atualizar_meta.titulo = titulo_input
            atualizar_meta.descricao = descricao_input
            db.session.commit()
            return redirect(url_for('metas'))
    return render_template('editar_metas.html', atualizar_meta = atualizar_meta)

@app.route("/apagar_metas/<idmeta>",methods=['GET','POST'])
@login_required
def apagar_metas(idmeta):    
    apagar_meta = Meta.query.filter_by(id = idmeta).first()
    db.session.delete(apagar_meta)
    db.session.commit()
    return redirect(url_for('metas'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

