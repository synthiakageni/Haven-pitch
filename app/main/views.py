from flask import render_template,request,url_for,abort,redirect
from . import main
from flask_login import login_required, current_user
from ..models import Comments, User,Role,Categories,Pitches,Comments,Upvotes,Downvotes
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db
import markdown2


@main.route('/')
def index():
    
    category = Categories.query.all()
    
    
    return render_template('profile/index.html',categories = category)

@main.route('/pitch/<int:id>')
def pitch(id):
        category = Categories.query.filter_by(id=id).first().id
        title =Categories.query.filter_by(id=id).first().category
        pitches = Pitches.get_pitch(category)
        
        return render_template('pitch.html',title=title,category=category,pitches=pitches)
    
@main.route('/comment/<int:id>')
def comment(id):
    pitch = Pitches.query.filter_by(id=id).first().id
    comments = Comments.get_comments(pitch)
    
    return render_template('comment.html',pitch=pitch,comments=comments)   

    

@main.route('/pitch/new/<int:id>', methods=['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    cat = Categories.query.filter_by(id=id).first().id
    
    if form.validate_on_submit():
        pitch = form.pitch.data
        category_id = Categories.query.filter_by(id=id).first().id

        
        new_pitch = Pitches(pitch=pitch, category_id=category_id,user=current_user)
        
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html', pitch_form=form)

@main.route('/<int:id>')
def single_pitch(id):
    pitch=Pitches.query.get(id)
    if pitch is None:
        abort(404)
    format_pitch = markdown2.markdown(pitch.pitch,extras=["code-friendly", "fenced-code-blocks"])    
    return render_template('index.html',pitch = pitch, format_pitch=format_pitch)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user=user)    

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile', uname=user.username))
    
    return render_template('profile/update.html',form=form)    

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    

@main.route('/pitch/comment/new/<int:id>',methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = Pitches.query.filter_by(id=id).first().id
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = Pitches.query.filter_by(id=id).first().id
        
        new_comment=Comments(comment=comment,pitch_id=pitch_id,user=current_user)
        db.session.add(new_comment)
        db.session.commit()
       # return redirect(url_for('main.index/pitch'))
        return redirect(url_for('main.comment',id = pitch_id ))

        
    title = 'Comment...'
    return render_template('new_comment.html',title=title,comment_form=form)    

@main.route('/comment/<int:id>')
def single_comment(id):
    comment=Comments.query.get(id)
    if comment is None:
        abort(404)
        format_comment = markdown2.markdown(comment.comment,extras=["code-friendly", "fenced-code-blocks"])
        
        return redirect(url_for('main.index'))

        return render_template('index.html',comment=comment,format_comment=format_comment)
    
@main.route('/pitch/upvote/new/<int:id>', methods=['GET','POST'])
@login_required
def upvote(id):
        get_ps = Upvotes.get_upvotes(id)
        valid_string = f'{current_user.id}:{id}'
        for pitch in get_ps:
            to_str = f'{pitch}'
            print(valid_string+" "+to_str)
            if valid_string == to_str:
                return redirect(url_for('main.index',id=id))
            else:
                continue
        new_vote = Upvotes(user = current_user, pitch_id=id)
        new_vote.save()
        return redirect(url_for('main.upvote',id=id))    
        
@main.route('/pitch/downvote/new/<int:id>', methods=['GET','POST'])
@login_required
def downvote(id):
        get_ds = Downvotes.get_downvotes(id)
        valid_string = f'{current_user.id}:{id}'
        for pitch in get_ds:
            to_str = f'{pitch}'
            print(valid_string+" "+to_str)
            if valid_string == to_str:
                return redirect(url_for('main.index',id=id))
            else:
                continue
        new_vote = Downvotes(user = current_user, pitch_id=id)
        new_vote.save()
        return redirect(url_for('main.downvote',id=id))    
                
    


    
    