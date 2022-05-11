from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField ,SubmitField
from wtforms.validators import DataRequired


CATEGORY_CHOICES=[('Life Pitch','Life Pitch'), ('Business Pitch','Business Pitch'), ('Elevator Pitch','Elevator Pitch'), ('Inspiration Pitch','Inspiration Pitch'), ('Personal Pitch','Personal Pitch'), ('Puns','Puns')]

class EditProfile(FlaskForm):
    about = TextAreaField('Tell us about yourself.',validators = [DataRequired()])
    submit = SubmitField('Update')


class PitchForm(FlaskForm):
    pitch_category = SelectField('Choose a category', choices=CATEGORY_CHOICES, validators=[DataRequired()])
    pitch_text = TextAreaField('Your pitch here', validators=[DataRequired()]) 
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    pitch_comment = TextAreaField('Make a comment', validators=[DataRequired()])
    submit = SubmitField('Comment')