"""
The flask application package.
"""

from flask import Flask
from .views.profile import profile

app = Flask(__name__)
app.register_blueprint(profile)