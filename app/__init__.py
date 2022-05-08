from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy()

# Initializing application
def create_app(config_name):
    app = Flask(__name__)

    
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)


# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_object(config_options[config_name])


from app import views