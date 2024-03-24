#!/usr/bin/python3

""" simple flask program"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ function to diplay hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def fun_HBNB():
    """ function to diplay HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_HBNB(text):
    """ function to diplay C <text>"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_HBNB(text):
    """ function to diplay python <text>"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_number_HBNB(n):
    """ function to diplay the number passed"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def page_number_HBNB(n):
    """ function to diplay the html page if passed an integer"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even_HBNB(n):
    """ function to diplay the html page if passed an odd or even integer"""
    type_num = "odd"
    if n % 2 == 0:
        type_num = "even"
    return render_template('6-number_odd_or_even.html', number=n, tye=type_num)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
