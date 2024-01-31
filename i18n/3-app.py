#!/usr/bin/env python3
"""
Task 3
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config():
    """ Configuration class """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)


@app.route('/')
def index():
    """ Routeds to 3-index """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ Returns the best language match """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
