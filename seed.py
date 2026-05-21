# seed.py

from app import app, db, Produto, Usuario

with app.app_context():
    db.create_all()

    if Produto.query.count() == 0:
        db.session.add_all([
            Produto(nome='Notebook' , preco=3500.00),
            Produto(nome='Mouse'    , preco=99.99),
            Produto(nome='Teclado'  , preco=149.90),
            Produto(nome='Filtro de Linha', preco=50.00),
            Produto(nome='Mouse Pad', preco=14.49),
        ])

        # Confirmar a gravação dos dados
        db.session.commit()
        print('Produtos Criados com Sucesso!')
    
    if Usuario.query.count() == 0:
        admin = Usuario(email='admin@fasm.com')
        admin.set_senha('123456')

        db.session.add(admin)
        
        # Confirmar a gravação dos dados
        db.session.commit()
        print('Usuários criados com Sucesso!')