"""
The flask application package.
"""

from flask import Flask
from .views.profile import profile
from flask_bootstrap import Bootstrap
import json


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))


bootstrap = Bootstrap()

app = Flask(__name__)

bootstrap.init_app(app)
app.jinja_env.filters['tojson_pretty'] = to_pretty_json
app.register_blueprint(profile)
