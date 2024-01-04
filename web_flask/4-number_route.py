#!/usr/bin/python3
"""Starts a Flask web application

The application listens on 0.0.0.0:5000
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: displays "HBNB"
    /c/<text>: displays C followed by value of <text>
    /
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display sa"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display puthonat text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """ asdasda asdasd """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
