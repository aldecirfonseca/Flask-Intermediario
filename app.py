from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY']                        = 'fasm-2026-3p'
app.config['SQLALCHEMY_DATABASE_URI']           = 'sqlite:///banco.db'
# Desativa o monitoramento de alterações nos objetos da base de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']    = False

# criando o objeto db, que vai conectar com a base, criar tabelas, fazer consultas
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para continuar...'

# classe modelo Produto
"""
A classe gera e executa este comando na base de dados
CREATE TABLE produto (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco FLOAT NOT NULL
);
"""
class Produto(db.Model):
    __tablename__ = 'produto'
    id      = db.Column(db.Integer, primary_key=True)
    nome    = db.Column(db.String(100), nullable=False)
    preco   = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<produto {self.nome}>'

# classe modelo Usuário
class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash  = db.Column(db.String(256))

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha) 

#
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, int(user_id))

# Define o formulário de login
class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Entrar')

@app.route("/")
def index():
    return render_template(
            'index.html',
            titulo='Loja FASM'
        )

@app.route("/produto")
def produto():
    produtos = Produto.query.all()

    return render_template(
            'produto.html',
            titulo='Loja FASM',
            produtos=produtos
        )

@app.route("/sobrenos")
def sobrenos():
    return render_template(
        "sobrenos.html",
        titulo="Sobre nós",
        mensagem=""
    )

# Rota Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if usuario and usuario.check_senha(form.senha.data):
            login_user(usuario)
            return redirect(url_for('produto'))
        
        flash('E-mail ou senha Inválidos.', 'erro')

    return render_template(
            "login.html", 
            form=form,
            titulo="Login" 
        )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Criando a base de dados se não existir
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)