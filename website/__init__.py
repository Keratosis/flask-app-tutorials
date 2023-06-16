
#placing the __init__ in a folder makes it  a python package  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path # importing path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():  
    app = Flask(__name__) #, it represents the name of the file in which this code is written
    app.config['SECRET_KEY'] = 'youguysaregettingpaid' #secure the cookies in website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) #initialising database with app
    
   
    from .view import view 
    from .auth import auth
      
    
    app.register_blueprint(view, url_prefix ="/")
    app.register_blueprint(auth, url_prefix ="/")
    
    from .model import User
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader 
    def load_user(id):
        return User.query.get(int(id)) #look for primary key
    # how we load a user by their id
    
     
    return app

def create_database(app):
    #create database if it doesnot exist
    if not path.exists('website/'+ DB_NAME):
        with app.app_context():
            db.create_all()
        
        print('Database created!')
    
