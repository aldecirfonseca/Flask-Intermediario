from flask import Flask
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']                        = 'fasm-2026-3p'
    app.config['SQLALCHEMY_DATABASE_URI']           = 'sqlite:///banco.db'
    # Desativa o monitoramento de alterações nos objetos da base de dados
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']    = False

    db.init_app(app)
    login_manager.init_app(app)

    from blueprints.main import main_bp
    from blueprints.auth import auth_bp
    from blueprints.produtos import produtos_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(produtos_bp)

    # Criando a base de dados se não existir
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)