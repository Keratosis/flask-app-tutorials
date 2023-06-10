from flask import Blueprint, render_template
#By using blueprints, you can split your application into multiple modules, each responsible for its own set of routes and views. 

auth = Blueprint('auth',__name__)

@auth.route('/auth')
def  auth_page():
    return  render_template("auth.html")

@auth.route('/login')
def login():
    return render_template("login.html",text =" hello")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/preview')
def preview():
    return render_template("preview.html")
    