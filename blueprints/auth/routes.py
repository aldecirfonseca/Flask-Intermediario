from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from blueprints.auth import auth_bp
from models import Usuario
from forms import LoginForm

# Rota Login
@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if usuario and usuario.check_senha(form.senha.data):
            login_user(usuario)
            return redirect(url_for('produtos.produto'))
        
        flash('E-mail ou senha Inválidos.', 'erro')

    return render_template(
            "auth/login.html", 
            form=form,
            titulo="Login" 
        )

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
