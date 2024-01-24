#!/usr/bin/env python3
""" Session Authentication views
"""
from flask import Flask, request, jsonify, make_response
from api.v1.views import app_views
from models.user import User

app = Flask(__name__)


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ Handles authentication for Session """
    from api.v1.app import auth
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user[0].id)
    user_dict = user[0].to_json()

    response = make_response(jsonify(user_dict))
    response.set_cookie(app.config.get("SESSION_NAME", "_my_session_id"), session_id)

    return response
