#!/usr/bin/env python3
"""
Task 6 - Basic Flask app
"""
from flask import Flask, jsonify, request, abort, make_response
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
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        if not AUTH.valid_login(email, password):
            abort(401)

        session_id = AUTH.create_session(email)

        response = make_response(jsonify({"email": email, "message": "logged in"}))
        response.set_cookie("session_id", session_id)
        return response

    except:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
