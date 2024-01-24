#!/usr/bin/env python3
""" Session Authentication views
"""
from flask import Flask, request, jsonify, make_response
from api.v1.views import app_views
import os
from models.user import User




@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Handles authentication for Session """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    from models.user import User

    users = User.search({'email': email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    from os import getenv
    session_name  = getenv('SESSION_NAME')
    response = make_response(user.to_json())
    response.set_cookie(session_name, session_id)

    return response
