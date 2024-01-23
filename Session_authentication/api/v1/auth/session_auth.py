#!/usr/bin/env python3
""" Task 1 - Empty session
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class that inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a new session ID for a user """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Get the user ID for a session"""
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a User based on cookie value """
        cookie_value = self.session_cookie(request)
        if cookie_value is None:
            return None
        user_id = self.user_id_for_session_id(cookie_value)
        if user_id is None:
            return None

        user_instance = User.get(user_id)
        return user_instance
