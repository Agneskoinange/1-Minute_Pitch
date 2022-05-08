from flask import render_template,request,redirect,url_for,abort
from flask import render_template
from pip import main
from app import app
from flask_login import current_user, login_required
from ..models import User, Pitches
from .forms import EditProfile, PitchForm, CommentForm
from .. import db, photos
import markdown2  

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
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        category=pitch_form.pitch_category.data
        text = pitch_form.pitch_text.data
        new_pitch = Pitches(category=category, text=text, user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('index.home'))
    return render_template('new_pitch.html', pitch_form=pitch_form, )

@main.route('/user/<name>', methods=['GET','POST'])
@login_required
def profile(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)

    form=EditProfile()
    if form.validate_on_submit():
        user.about=form.about.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', name=user.username))
    return render_template('profile/profile.html', user=user )

@main.route('/user/<name>/edit/pic', methods=['POST'])
@login_required
def update_pic(name):
    user=User.query.filter_by(username=name).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.avatar=path
        db.session.commit()
    return redirect(url_for('main.profile', name=name))
