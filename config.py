import os 

class Config:
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://nessie:agnes1234@localhost/watchlist"
    SECRET_KEY = os.environ.get("SECRET_KEY'")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    UPLOADED_PHOTOS_DEST ="app/static/photos"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
 
   
class ProdConfig(Config):
    # DATABASE_URL = os.environ.get("DATABASE_URL")
    # if DATABASE_URL.startswith('postgres://'):
    # QLALCHEMY_DATABASE_URI=DATABASE_URL.replace('postgres://','postgresql://',1)
    # else:
    #     SQLALCHEMY_DATABASE_URI=DATABASE_URL

    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://nessie:agnes1234@localhost/watchlist"
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
}