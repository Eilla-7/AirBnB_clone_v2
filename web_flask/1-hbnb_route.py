#!/usr/bin/python3

""" simple flask program"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function to diplay hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def fun_hbnb():
    """ function to diplay HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
