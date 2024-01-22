#!/usr/bin/env python3
"""
Task 3 - Auth class
"""

from flask import request
from typing import List, TypeVar


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
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        normalized_path = path.rstrip('/') if path else path
        return normalized_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Placeholder method for extracting authorization header.

        Args:
        - request: The Flask request object (default=None).

        Returns:
        - str: Always returns None for demonstration purposes.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for retrieving the current user.

        Args:
        - request: The Flask request object (default=None).

        Returns:
        - TypeVar('User'): Always returns None for demonstration purposes.
        """
        return None
