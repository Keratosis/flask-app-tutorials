from flask import Blueprint
#By using blueprints, you can split your application into multiple modules, each responsible for its own set of routes and views. 

auth = Blueprint('auth',__name__)

@auth.route('/auth')
def  auth_page():
    return 'you are in the auth page'

@auth.route('/login')
def login():
    return "<p>login</P>"

@auth.route('/logout')
def logout():
    return "<p>logout</P>"

@auth.route('/sign_up')
def sign_up():
    return '<p>sign_up</P>'

@auth.route('/home')
def home():
    return '<p>home</P>'
    