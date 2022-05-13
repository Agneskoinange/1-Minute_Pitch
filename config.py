import os 
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    '''
    General configuration parent class
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'pitches.db')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nessie:agnes1234@localhost/pitches'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///pitches.db"

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

   

class ProdConfig(Config):
    # DATABASE_URL = os.environ.get("DATABASE_URL")
    # if DATABASE_URL.startswith('postgres://'):
    #     SQLALCHEMY_DATABASE_URI=DATABASE_URL.replace('postgres://','postgresql://',1)
    # else:
    #     SQLALCHEMY_DATABASE_URI=DATABASE_URL
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nessie:agnes1234@localhost/pitches_test'


class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nessie:agnes1234@localhost/pitches'
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}