# from multiprocessing import managers
# from app import app
from app import create_app,db
from app.models import User, Pitches
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

@app.route('/')
def getting_started():
    return 'Are you ready?' 
from app import app 