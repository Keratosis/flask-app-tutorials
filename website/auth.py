from flask import Blueprint, render_template,request,flash,redirect,url_for
from .model import User 
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

#By using blueprints, you can split your application into multiple modules, each responsible for its own set of routes and views. 
#request getting data from the server
auth = Blueprint('auth',__name__)

@auth.route('/auth')
@login_required 
def  auth_page():
    return  render_template("auth.html")

@auth.route('/login', methods =["GET",'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("login successfully!",category = 'success')
                login_user(user, rememder=True)
                #Remembers the user if hes logged in
                return redirect(url_for('view.home'))
            else:
                flash('password is incorrect,try again',category = 'error')
        else:
            flash('email does not exist')
                
    return render_template("login.html") 

@auth.route('/logout')
@login_required #this route can't be accessed unless the user is logged in
def logout():
    logout_user() #logs out te current user 
    
    # return render_template("logout.html")
    return redirect(url_for('auth.login'))
#returns the user to the loggin page

@auth.route('/sign_up',methods =["GET",'POST']) # METHODS allow the http request in the current page 
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('email already exists.',category =' success')
        elif len(email) < 4 :
            flash('Email must be greater than 4 characters.', category ="error")
            #category displays message
        elif len(firstName) <2:
            flash('firstName must be greater than 1 character.',category ="error")
        elif password1 != password2:
            flash('Password don\'t match.',category ="error")
        elif len(password1) < 7:
            flash('Password must be at least  characters.', category = 'error')
        else:
            new_user = User(email=email,first_name=firstName,password = generate_password_hash(password1,method ='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember = True)
            flash ('Account created!', category ="success")
            # add to database
            return redirect(url_for('view.home'))
            
        
        
        
    return render_template("sign_up.html")

@auth.route('/preview')
@login_required 
def preview():
    return render_template("preview.html")
    