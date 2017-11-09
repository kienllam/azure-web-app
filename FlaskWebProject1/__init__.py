"""
The flask application package.
"""

from flask import Flask
from .views.profile import profile
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

app = Flask(__name__)

bootstrap.init_app(app)
app.register_blueprint(profile)
