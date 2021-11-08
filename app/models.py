from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitches', backref = 'user', lazy = "dynamic")
    comment = db.relationship('Comments', backref = 'user', lazy = "dynamic")
    upvote = db.relationship('Upvotes', backref = 'user', lazy = "dynamic")
    downvote = db.relationship('Downvotes', backref = 'user', lazy = "dynamic")   
    pass_secure = db.Column(db.String(255))

        
    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
            
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)    

    
class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy="dynamic")
    
    def __repr__(self):
        return f'User {self.name}'   
    
class Categories(db.Model):
    
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.category}'   
 
    def save_category(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_categories(cls):
        categories = Categories.query.all()    
        return categories
     
    
    
class Pitches(db.Model):
    
    __tablename__= 'pitch'
    
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String)
    category_id = db.Column(db.Integer)
    owner = db.Column(db.Integer,db.ForeignKey('users.id'))
    upvote = db.relationship('Upvotes', backref = 'pitch', lazy = "dynamic")
    downvote = db.relationship('Downvotes', backref = 'pitch', lazy = "dynamic")
    

    def __repr__(self):
        return f'User {self.pitch}' 
        
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
     
    @classmethod   
    def get_pitch(cls,id):
        pitches = Pitches.query.filter_by(category_id = id).all()
        
        return pitches  
    
            
class Comments(db.Model):
    
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    pitch_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
      
    @classmethod  
    def get_comments(cls,id): 
        comments = Comments.query.filter_by(pitch_id=id).all()   
        return comments
    
class Upvotes(db.Model):
    
    __tablename__ = 'upvotes' 
    
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
      
    @classmethod  
    def get_upvotes(cls,id): 
        upvotes = Upvotes.query.filter_by(pitch_id=id).all()   
        return upvotes
    
    
       
class Downvotes(db.Model):
    
    __tablename__ = 'downvotes' 
    
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
      
    @classmethod  
    def get_downvotes(cls,id): 
        downvotes = Downvotes.query.filter_by(pitch_id=id).all()   
        return downvotes
    
    
       



    
    

      

    