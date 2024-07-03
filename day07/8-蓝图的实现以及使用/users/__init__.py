from flask import Blueprint
from . import views

users_app = Blueprint('users', __name__,
                      url_prefix='/users', static_folder='static', template_folder='template')

users_app.add_url_rule('/login', view_func=views.login)
users_app.add_url_rule('/register', view_func=views.register)
users_app.add_url_rule('/demo', view_func=views.demo)
