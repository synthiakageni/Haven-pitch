from flask import render_template,redirect,url_for,flash,request
from ..models import Categories
from .forms import CategoryForm
from flask_login import login_required, current_user
from . import cats
from .. import db
from ..main import  main

@cats.route('/category',methods=["GET","POST"])
@login_required
def category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Categories(category = form.category.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('main.index'))

    #flash('category added successfully')
    #title = "New Category"
    return render_template('cats/category.html',category_form = form)
