from flask import Blueprint, render_template
from flask_login import login_user,login_required,logout_user,current_user

#By using blueprints, you can split your application into multiple modules, each responsible for its own set of routes and views. 

view = Blueprint('view',__name__)


@view.route('/') #defining a route
@login_required # user cant access the home page unless his logged in 
def home():
    return  render_template("home.html")
    