# Flask — Módulo 2: Intermediário

**Disciplina:** Técnicas de Programação  
**Instituição:** Faculdade Santa Marcelina — FASM, Muriaé/MG  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Professor:** Aldecir Fonseca  
**Ano:** 2026

---

## Sobre o Módulo

Este módulo aprofunda o desenvolvimento web com Flask, introduzindo banco de dados relacional, autenticação de usuários, organização modular com Blueprints e interface responsiva com Bootstrap 5. Corresponde ao **Bloco 2 — Intermediário** da Disciplina Técnicas de Programação, Curso de Flask — Python para Desenvolvimento Web (aulas 5 a 8).

---

## Conteúdo das Aulas

| Aula | Tópico | Conceitos |
|------|--------|-----------|
| 5 | Banco de Dados com SQLAlchemy | ORM, modelos, CRUD, Flask-SQLAlchemy |
| 6 | Autenticação com Flask-Login | Login, logout, sessão, hashing de senhas |
| 7 | Blueprints — Organização Modular | Application Factory, módulos independentes |
| 7+ | Interface com Bootstrap 5 | Templates responsivos, Bootstrap Icons, CSS customizado |
| 8 | API REST com Flask | JSON, endpoints RESTful, HTTP methods *(em breve)* |

---

## Estrutura do Projeto

```
2_INTERMEDIARIO/
├── app.py                      # Application Factory (create_app)
├── extensions.py               # Instâncias de db e login_manager
├── models.py                   # Modelos Produto e Usuario
├── forms.py                    # Formulário de login (Flask-WTF)
├── seed.py                     # Popula o banco com dados iniciais
├── banco.db                    # Banco de dados SQLite (gerado automaticamente)
├── blueprints/
│   ├── main/                   # Blueprint principal (index, sobrenos)
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── auth/                   # Blueprint de autenticação (login, logout)
│   │   ├── __init__.py
│   │   └── routes.py
│   └── produtos/               # Blueprint de produtos
│       ├── __init__.py
│       └── routes.py
├── static/
│   └── css/
│       └── style.css           # Estilos customizados (cores e identidade FASM)
├── templates/
│   ├── base.html               # Layout base com navbar, footer e Bootstrap 5
│   ├── main/
│   │   ├── index.html          # Página inicial com cards e hero section
│   │   └── sobrenos.html       # Página "Sobre nós"
│   ├── auth/
│   │   └── login.html          # Formulário de login com validação
│   └── produtos/
│       └── produto.html        # Listagem de produtos em tabela estilizada
└── venv/                       # Ambiente virtual Python
```

---

## Tecnologias e Extensões

- **Flask** — micro-framework web
- **Flask-SQLAlchemy** — ORM para banco de dados relacional
- **Flask-Login** — gerenciamento de sessão e autenticação
- **Flask-WTF / WTForms** — formulários com validação e proteção CSRF
- **Werkzeug** — hashing seguro de senhas
- **SQLite** — banco de dados local (arquivo `banco.db`)
- **Bootstrap 5.3.3** — framework CSS para interface responsiva
- **Bootstrap Icons 1.11.3** — biblioteca de ícones SVG

---

## Modelos de Dados

### Produto
```python
class Produto(db.Model):
    __tablename__ = 'produto'
    id      = db.Column(db.Integer, primary_key=True)
    nome    = db.Column(db.String(100), nullable=False)
    preco   = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<produto {self.nome}>'
```

### Usuario
```python
class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash  = db.Column(db.String(256))

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
```

---

## Rotas da Aplicação

| Blueprint | Método | Rota | Descrição |
|-----------|--------|------|-----------|
| `main` | GET | `/` | Página inicial com hero e cards informativos |
| `main` | GET | `/sobrenos` | Página sobre nós com informações do curso |
| `auth` | GET / POST | `/login` | Formulário de login com validação Flask-WTF |
| `auth` | GET | `/logout` | Encerra a sessão e redireciona para login |
| `produtos` | GET | `/produto` | Listagem de produtos com preços |

---

## Como Executar

### 1. Criar e ativar o ambiente virtual

```bash
# Criar
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
```

### 2. Instalar as dependências

```bash
pip install flask flask-sqlalchemy flask-login flask-wtf werkzeug
```

### 3. Popular o banco com dados iniciais (opcional)

```bash
python seed.py
```

Cria 5 produtos e o usuário `admin@fasm.com` com senha `123456`.

### 4. Executar a aplicação

```bash
python app.py
```

O banco de dados `banco.db` é criado automaticamente na primeira execução.  
Acesse em: **http://localhost:5000**

---

## Conceitos Aplicados

### Aula 5 — SQLAlchemy
- Configuração do `SQLALCHEMY_DATABASE_URI` com SQLite
- Definição de modelos como classes Python (`db.Model`) com `__tablename__` explícito
- Criação automática das tabelas com `db.create_all()`
- Operações CRUD via `db.session`

### Aula 6 — Flask-Login
- Modelo `Usuario` com `UserMixin` para integração com Flask-Login
- Hashing de senhas com `generate_password_hash` / `check_password_hash`
- Métodos `set_senha()` e `check_senha()` encapsulados no modelo
- Proteção de rotas com `@login_required`
- Controle de sessão com `login_user()` e `logout_user()`

### Aula 7 — Blueprints
- Separação da aplicação em módulos independentes (`main`, `auth`, `produtos`)
- Padrão **Application Factory** (`create_app()`) em `app.py`
- Extensões isoladas em `extensions.py` para evitar importações circulares
- Registro de blueprints com `app.register_blueprint()`

### Aula 7+ — Bootstrap 5 e Templates Responsivos
- Layout base em `base.html` com navbar colapsável e footer responsivo
- Identidade visual FASM com variáveis CSS customizadas (`--fasm-azul`, `--fasm-vermelho`)
- Uso de Bootstrap Icons nos elementos de navegação e conteúdo
- Componentes Bootstrap: cards, tabelas, badges, alertas e botões
- Mensagens flash com `get_flashed_messages()` e alertas dismissíveis
- Exibição condicional na navbar: email do usuário e botão "Sair" quando autenticado
- Formulário de login com feedback visual de erros de validação (`is-invalid`)
- Arquivo de estilos em `static/css/style.css` carregado via `url_for('static', ...)`

---

## Referências

- [Documentação Flask](https://flask.palletsprojects.com)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com)
- [Flask-Login](https://flask-login.readthedocs.io)
- [WTForms](https://wtforms.readthedocs.io)
- [Bootstrap 5](https://getbootstrap.com/docs/5.3)
- [Bootstrap Icons](https://icons.getbootstrap.com)

---

*Aulas ministradas pelo Professor Aldecir Fonseca — FASM Muriaé, MG*
