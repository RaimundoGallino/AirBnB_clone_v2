#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """starts a Flask web application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """starts a Flask web application"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """starts a Flask web application"""
    text.replace("_", " ")
    return "C " + text


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def display_python_text(text="is cool"):
    """starts a Flask web application"""
    text.replace("_", " ")
    return "Python " + text


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
