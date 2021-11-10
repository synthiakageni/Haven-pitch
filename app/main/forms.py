from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,RadioField
from wtforms import validators
from wtforms.validators import Email,EqualTo
from ..models import User,Categories
from wtforms import ValidationError
from wtforms.validators import InputRequired


class PitchForm(FlaskForm):
    pitch = TextAreaField('Pitch', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment =   TextAreaField('Add Your Comment Here...') 
    submit = SubmitField('Submit')

    


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
class Categories(FlaskForm):
    category = StringField('Category', validators=[InputRequired()])
    submit = SubmitField('submit')
        