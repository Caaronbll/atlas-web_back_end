#!/usr/bin/env python3
"""
Task 6 - Basic Flask app
"""
from flask import Flask, jsonify, request, abort, make_response
from flask import redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome():
    """ Returns a message """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user():
    """ Registers a user """
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200

    except Auth.UserAlreadyExistsError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ Login to the session """
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = make_response(jsonify({"email": email,
                                      "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Logs out of the session """
    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route('/profile', methods=['GET'])
def profile():
    """ Finds user from session ID """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """ Generates token from email """
    try:
        email = request.form.get("email")
        reset_token = AUTH.get_reset_password_token(email)
        if reset_token:
            return jsonify({"email": email, "reset_token": reset_token}), 200
        else:
            abort(403)
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
