#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.teardown_appcontext
def storage_close(a):
    """starts a Flask web application"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states()
    """list_states"""
    list_states = storage.all(State).values()
    return render_template('7-states_list.html', list_states=list_states)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)