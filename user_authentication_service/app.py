#!/usr/bin/env python3
"""
Task 6 - Basic Flask App
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slaches=False)
def welcome() -> str:
    """ returns message from api"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slaches=False)
def register_users(email: str, password: str):
    """Endpoint to register a user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
