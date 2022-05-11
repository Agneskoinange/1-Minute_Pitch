from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField ,ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User


class SignupForm(FlaskForm):
    username = StringField('Enter your name', validators=[DataRequired()])
    email = StringField('Enter your email address', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('A user with that email address exists')
    
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('THis username is already taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')