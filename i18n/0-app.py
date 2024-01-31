#!/usr/bin/env python3
"""
Task 0
"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=['GET'])
def index():
    """ Routeds to 0-index """
    return render_template('templates/0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
