from app import app
from flask import render_template,request,redirect,url_for,abort
from . import main
# from app import app
from flask_login import current_user, login_required
from ..models import User, Pitches, Comments
from .forms import EditProfile, PitchForm, CommentForm
from .. import db, photos
# import markdown2  

# Views

@main.route('/')
def home():

    '''
    View root page function that returns the home page and its data
    '''
    pitches=Pitches.query.all()
    identification = Pitches.user_id
    posted_by = User.query.filter_by(id=identification).first()
    user = User.query.filter_by(id=current_user.get_id()).first()

    return render_template('pitches.html', pitches=pitches, posted_by=posted_by, user=user)


@main.route('/new_pitch', methods=['GET','POST'])
@login_required
def pitch_form():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        category=pitch_form.pitch_category.data
        text = pitch_form.pitch_text.data
        new_pitch = Pitches(category=category, text=text, user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.home'))
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
    return render_template('profile/profile.html', user=user, form=form )

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


@main.route('/categories/<pitch_category>')
def categories(pitch_category):
    pitch = Pitches.get_category(pitch_category)

    identification = Pitches.user_id
    posted_by = User.query.filter_by(id=identification).first()
    return render_template('categories.html', pitch=pitch, posted_by=posted_by)


@main.route('/comments/<int:pitch_id>', methods=['GET','POST'])
@login_required
def pitch_comments(pitch_id):
    comments = Comments.get_comments(pitch_id)

    pitch = Pitches.query.get(pitch_id)
    pitch_posted_by = pitch.user_id
    user = User.query.filter_by(id=pitch_posted_by).first()

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.pitch_comment.data      
        new_comment = Comments(comment=comment, pitch_id=pitch_id, user_id=current_user.get_id())
        new_comment.save_comment()
        return redirect(url_for('main.pitch_comments',pitch_id = pitch_id))

    return render_template('comments.html', comment_form=form, comments=comments, pitch = pitch, user=user)
