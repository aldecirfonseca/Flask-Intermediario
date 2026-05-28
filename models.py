from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db, login_manager

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
