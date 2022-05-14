import os 


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY'")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    UPLOADED_PHOTOS_DEST ="app/static/photos"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")

   

class ProdConfig(Config):
    pass

class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://nessie:agnes1234@localhost:5432/watchlist"
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}