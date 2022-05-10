from flask import Flask

app = Flask(__name__)

@app.route('/')
def getting_started():
    return 'Are you ready?' 
from app import app 