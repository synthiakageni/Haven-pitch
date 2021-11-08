from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired
from ..models import Categories

class CategoryForm(FlaskForm):
        category = StringField('Enter Your Category',validators=[InputRequired()])
        submit = SubmitField('Add Category')
