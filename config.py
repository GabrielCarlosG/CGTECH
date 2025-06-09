from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """Configurações gerais da aplicação."""
    
    # Chave secreta para sessões e CSRF (Cross-Site Request Forgery)
    SECRET_KEY = os.getenv('SECRET_KEY', 'sua-chave-secreta-aqui')
    
    # Configurações de caminho para diretórios estáticos e templates
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'
    
    # Configurações de segurança para cookies de sessão (opcional)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True  # Ativar True quando estiver em produção

    # Banco de Dados
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///mensagens.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #removendo a configuração de email, por enquanto!!!!!
    # Configurações de E-mail
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = 'cgtech.tec.br'  # Seu e-mail
    # MAIL_PASSWORD = '1245!@#QWe'  # Sua senha ou token de app
    # MAIL_DEFAULT_SENDER = 'contato@cgtech.tec.br'  # E-mail de envio