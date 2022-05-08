from . import auth
from flask import render_template,redirect,url_for, flash,request
from ..models import User
from .forms import LoginForm, SignupForm
from flask_login import login_user,logout_user,login_required
from .. import db

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.check_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))

        flash('Invalid username or Password')

    title = "User login"
    return render_template('auth/login.html',login_form = login_form,title=title)



@auth.route('/signup', methods=['GET', 'POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        # db.session.add(user)
        # db.session.commit()
        # mail_message('Welcome to pitch', 'email/welcome_user', user.email, user=user)
        # return redirect(url_for('auth.login'))
        # title = "Create account"
    return render_template('auth/signup.html', signup_form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))