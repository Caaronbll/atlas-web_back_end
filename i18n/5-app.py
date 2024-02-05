#!/usr/bin/env python3
"""
Task 3
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Configuration class """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def index():
    """ Routeds to 3-index """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ Returns the best language match """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Returns a user dictionary """
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    try:
        user_id = int(user_id)
        if user_id < 1 or user_id > 4:
            raise Exception
    except Exception:
        return None
    return users[user_id]



if __name__ == '__main__':
    app.run(debug=True)
