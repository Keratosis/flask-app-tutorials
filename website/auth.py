from flask import Blueprint, render_template,request
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
        pass
        
        
    return render_template("sign_up.html")

@auth.route('/preview')
def preview():
    return render_template("preview.html")
    