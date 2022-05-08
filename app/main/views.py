from flask import render_template
from pip import main
from app import app

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/pitches')
def pitches():

    '''
    View Pitch page function that returns the Pitch details page and its data
    '''
    return render_template('pitches.html', pitches=pitches)