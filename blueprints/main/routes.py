from flask import render_template
from blueprints.main import main_bp

@main_bp.route('/')
def index():
    return render_template(
        'main/index.html',
        titulo='Loja FASM'
    )

@main_bp.route('/sobrenos')
def sobrenos():
    return render_template(
        'main/sobrenos.html',
        titulo="Sobre nós"
    )