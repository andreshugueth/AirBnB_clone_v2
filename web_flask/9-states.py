#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def index(id):
    """renders an HTML with a list of states"""
    states = storage.all("State").values()
    if id is not None:
        state_id = 'State.{}'.format(id)
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
