import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config
from config import DevConfig
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

app = Flask(__name__)
login_manager = LoginManager()
login_manager.session_protection = 'string'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
app.config.from_object(Config)
db = SQLAlchemy(app)
photos = UploadSet('photos',IMAGES)
mail = Mail()

# Initializing application
def create_app(config_name):
    app = Flask(__name__)

    
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    # db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # simple.init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # Setting up configuration
    # app.config.from_object(Config)
    app.config.from_object(DevConfig)
    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_DATABASE_URL'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://nessie:agnes1234@localhost:5433/pitches'
    app.config["SECRET_KEY"] = 'agnes1234'

    # configure UploadSet
    configure_uploads(app,photos)
    

    return app

# from app import views
