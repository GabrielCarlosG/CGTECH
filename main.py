# app.py
from myapp import  create_app  # Importa a instância Flask do app/__init__.py
from myapp import db
from myapp.models import Mensagem

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)