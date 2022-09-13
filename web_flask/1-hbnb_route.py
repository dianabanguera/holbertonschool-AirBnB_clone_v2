#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hellos HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index1():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
