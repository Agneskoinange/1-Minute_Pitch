from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField ,SubmitField
from wtforms.validators import Required

CATEGORY_CHOICES=[('Elevator Pitch','Elevator Pitch'), ('Pickup lines','Pickup lines'), ('Puns','Puns')]

class EditProfile(FlaskForm):
    about = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Update')

class PitchForm(FlaskForm):
    pitch_category = SelectField('Choose a category', choices=CATEGORY_CHOICES, validators=[Required()])
    pitch_text = TextAreaField('Your pitch here', validators=[Required()]) 
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    pitch_comment = TextAreaField('Make a comment', validators=[Required()])
    submit = SubmitField('Comment')