from flask import Blueprint
#By using blueprints, you can split your application into multiple modules, each responsible for its own set of routes and views. 

auth = Blueprint('auth',__name__)

@auth.route('/auth')
def away():
    return 'you are in the auth page'
    
    