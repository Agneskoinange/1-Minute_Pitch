from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import DevConfig
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

# Initializing application
def create_app(config_name):
    app = Flask(__name__)

    
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # Setting up configuration
    app.config.from_object(DevConfig)
    app.config.from_object(config_options[config_name])


    return app

# from app import views