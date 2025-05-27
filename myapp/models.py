from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    assunto = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)
    snRespondido = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Mensagem {self.nome} - {self.assunto}>'
    
class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    resumo = db.Column(db.String(200), nullable=True)  # resumo opcional
    imagem_capa = db.Column(db.String(200), nullable=True)  # caminho para imagem
    slug = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f'<Noticia {self.titulo} - {self.slug}>'
    
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128))

    # relacionamento reverso: usuario.noticias
    noticias = db.relationship('Noticia', backref='autor', lazy=True)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f"<Usuario {self.nome}>"