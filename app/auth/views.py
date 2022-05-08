from flask import render_template
from . import auth
from flask import render_template,redirect,url_for
from ..models import User
from .forms import SignupForm
from .. import db

@auth.route('/login')
def login():
    return render_template('auth/login.html')



@auth.route('/signup', methods=['GET', 'POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message('Welcome to pitch', 'email/welcome_user', user.email, user=user)
        return redirect(url_for('auth.login'))
        title = "Create account"
    return render_template('auth/signup.html', signup_form=form)