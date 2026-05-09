from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY']                        = 'fasm-2026-3p'
app.config['SQLALCHEMY_DATABASE_URI']           = 'sqlite:///banco.db'
# Desativa o monitoramento de alterações nos objetos da base de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']    = False

# criando o objeto db, que vai conectar com a base, criar tabelas, fazer consultas
db = SQLAlchemy(app)

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
    produtos = [
        {'nome': 'Notebook', 'preco': 6499.99},
        {'nome': 'Mouse', 'preco': 75.99}
    ]

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
        # se os dados forem válidos, redireciona para index
        return render_template(
            'index.html',
            titulo='Login',
            mensagem=f"Login feito com sucesso para {form.email.data}"
        )

    return render_template(
            "login.html", 
            titulo="Login", 
            form=form
        )

# Criando a base de dados se não existir
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)