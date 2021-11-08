from flask import Blueprint

cats = Blueprint('cats',__name__)

from . import views