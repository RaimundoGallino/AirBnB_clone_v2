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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
