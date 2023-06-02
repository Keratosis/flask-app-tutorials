
#placing the __init__ in a folder it becomes a python package  
from flask import Flask

def create_app():
    app = Flask(__name__) #, it represents the name of the file in which this code is written
    app.config['SECRET_KEY'] = 'youguysaregettingpaid'
    
    return app
    
