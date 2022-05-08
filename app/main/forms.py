from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField ,SubmitField
from wtforms.validators import Required


class EditProfile(FlaskForm):
    about = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Update')