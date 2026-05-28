from flask import render_template
from blueprints.produtos import produtos_bp
from models import Produto

@produtos_bp.route("/produto")
def produto():
    produtos = Produto.query.all()

    return render_template(
            'produtos/produto.html',
            titulo='Loja FASM',
            produtos=produtos
        )
