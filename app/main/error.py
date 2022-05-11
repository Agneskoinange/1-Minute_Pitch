from flask import render_template
from . import main

@main.app_errorhandler(404)
def not_found(error):
    '''
    '''
    return render_template('not_found.html'),404