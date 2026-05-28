from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

# criando o objeto db, que vai conectar com a base, criar tabelas, fazer consultas
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para continuar...'