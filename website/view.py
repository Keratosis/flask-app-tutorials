from flask import Blueprint
#By using blueprints, you can split your application into multiple modules, each responsible for its own set of routes and views. 

view = Blueprint('view',__name__)


@view.route('/') #defining a route
def home():
    return 'Hello World! hold up'