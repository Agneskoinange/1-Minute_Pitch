import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'pitches.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nessie:agnes1234@localhost/pitches'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS='False'

    SQLALCHEMY_DATABASE_URI = "sqlite:///pitches.db"
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     'pool_size': 1
    # }

    # SQLALCHEMY_BINDS = {
    #     'db1': 'sqlalchemy://...'

    #     'db2': 'sqlalchemy://...'
    # }
    
    # SQLALCHEMY_BINDS_ENGINE_OPTIONS = {
    #     'db1': {'pool_size': 0}, # engine_options for 'db1' 
    #     'db2': {'pool_size': 0} # engine_options for 'db2' 
    # }

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

   

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')

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
