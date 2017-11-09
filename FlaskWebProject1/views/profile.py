from flask import Blueprint

profile = Blueprint('profile', __name__)

@profile.route('/')
@profile.route('/home')
def home():
    return 'Welcome Home'