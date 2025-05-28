# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from myapp import models


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return db.Usuario.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.secret_key = 'sua-chave-secreta-aqui'

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Importa e registra o blueprint
    from myapp.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Garante que os modelos sejam carregados
    from myapp import models

    return app