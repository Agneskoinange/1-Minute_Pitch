from app import app

@app.route('/')
def getting_started():
    return 'From views.py' 
