from . import db # from current package(website) import db
from flask_login import UserMixin #modules that helps with user login
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    data = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class User(db.Model, UserMixin):
    #defining a schema
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150),unique= True)
    password =db.Column(db.String(150),unique= True)
    first_name = db.Column(db.String(150),unique= True)
    note= db.relationship('Note')