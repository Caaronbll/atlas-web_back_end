#!/usr/bin/env python3
""" Task 1 - Session class
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from flask import Flask, request, jsonify, make_response
from api.v1.views import app_views

app = Flask(__name__)


class SessionAuth(Auth):
    """ Session class for authentication """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session ID for user """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns user ID for session """
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns user instance based on cookie value"""
        session_id = self.session_cookie(request)
        if session_id:
            user_id = self.user_id_for_session_id(session_id)
            if user_id:
                return User.get(user_id)

        return None

    @app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
    def auth_session_login():
        """ Handles authentication for Session """
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

        from api.v1.app import auth
        session_id = auth.create_session(user[0].id)
        user_dict = user[0].to_json()

        response = make_response(jsonify(user_dict))
        response.set_cookie(app.config.get("SESSION_NAME", "_my_session_id"), session_id)

        return response
