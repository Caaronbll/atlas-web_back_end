#!/usr/bin/env python3
"""
Task 3 - Auth class
"""

from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Placeholder method for checking authentication requirement.

        Args:
        - path (str): The path to check for authentication.
        - excluded_paths (List[str]): List of paths to be excluded.

        Returns:
        - bool: Always returns False for demonstration purposes.
        """
        if path is None or excluded_paths is None:
            return True
        if excluded_paths == []:
            return True
        if path[-1] == '/':
            normalized_path = path
        else:
            normalized_path = path + '/'
        for ex_path in excluded_paths:
            if ex_path[-1] != '/':
                ex_path = ex_path + '/'
        return bool(normalized_path not in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """
        Placeholder method for extracting authorization header.

        Args:
        - request: The Flask request object (default=None).

        Returns:
        - str: Always returns None for demonstration purposes.
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for retrieving the current user.

        Args:
        - request: The Flask request object (default=None).

        Returns:
        - TypeVar('User'): Always returns None for demonstration purposes.
        """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from request """
        if request is None:
            return None
        session_cookie_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_cookie_name)
