#!/usr/bin/python3
"""
script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def second_index():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """print C with a text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Return python and a text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_numeber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Display if a number is odd or even"""
    if n % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           even_or_odd=even_or_odd)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
