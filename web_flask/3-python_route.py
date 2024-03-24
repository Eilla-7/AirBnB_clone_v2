#!/usr/bin/python3

""" simple flask program"""

from flask import Flask
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
    """ function to diplay HBNB"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_HBNB(text):
    """ function to diplay HBNB"""
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
