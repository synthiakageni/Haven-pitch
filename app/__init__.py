
from flask import Flask
from .config import DevConfig
from .config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_uploads import UploadSet,configure_uploads,IMAGES
#from werkzeug.utils import secure_filename
#from werkzeug.datastructures import  FileStorage
import os
from flask_mail import Mail
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

mail = Mail()

bootstrap = Bootstrap()
db = SQLAlchemy()

#photos = UploadSet('photos', IMAGES)

simple = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)

    #app configurations
    app.config.from_object(config_options[config_name])
    #config_options[config_name].init_app(app)
    app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
    
    #configure UploadSet
    #configure_uploads(app,photos)
    
    #initialize bootstrap
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
    
    #register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    from .cats import cats as cats_blueprint
    app.register_blueprint(cats_blueprint,url_prefix='/categories')

    return app

