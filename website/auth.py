from flask import Blueprint, render_template,request,flash
#By using blueprints, you can split your application into multiple modules, each responsible for its own set of routes and views. 
#request getting data from the server
auth = Blueprint('auth',__name__)

@auth.route('/auth')
def  auth_page():
    return  render_template("auth.html")

@auth.route('/login', methods =["GET",'POST'])
def login():
    data = request.form # access data from our form in the login .
    print(data) #prints out the data in the terminal
    return render_template("login.html",text =" hello",boolean= False)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign_up',methods =["GET",'POST']) # METHODS allow the http request in the current page 
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4 :
            flash('Email must be greater than 4 characters.', category ="error")
            #category displays message
        elif len(firstName) <2:
            flash('firstName must be greater than 1 character.',category ="error")
        elif password1 != password2:
            flash('Password don\'t match.',category ="error")
        elif len(password1) < 7:
            flash('Password must be at least  characters.', category = 'error')
        else:
            flash('Account created!', category ="success")
            # add to database
            
        
        
        
    return render_template("sign_up.html")

@auth.route('/preview')
def preview():
    return render_template("preview.html")
    