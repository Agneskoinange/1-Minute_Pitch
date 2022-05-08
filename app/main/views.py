from flask import render_template
from pip import main
from app import app
from flask_login import current_user, login_required
from ..models import User, Pitches

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches=Pitches.query.all()
    identification = Pitches.user_id
    posted_by = User.query.filter_by(id=identification).first()
    user = User.query.filter_by(id=current_user.get_id()).first()

    return render_template('index.html', pitches=pitches, posted_by=posted_by, user=user)


@main.route('/new_pitch', methods=['GET','POST'])
@login_required
def pitch_form():
    # pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        category=pitch_form.pitch_category.data
        text = pitch_form.pitch_text.data
        new_pitch = Pitches(category=category, text=text, user=current_user)
        new_pitch.save_pitch()
        # return redirect(url_for('main.home'))
    return render_template('new_pitch.html', pitch_form=pitch_form, )