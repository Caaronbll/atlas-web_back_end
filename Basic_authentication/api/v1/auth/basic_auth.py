#!/usr/bin/env python3
""" Task 6 - Basic Authentication"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User
import binascii


class BasicAuth(Auth):
    """ Basic Auth class """
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """ Extract base64 authorization header """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        Decode the Base64 Authorization header to a UTF-8 string.

        Args:
        - base64_authorization_header (str): The Base64 Authorization header.

        Returns:
        - str: The decoded value as UTF-8 string.
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            base64_authorization_header = base64_authorization_header.encode(
                'utf-8')
            base64_authorization_header = b64decode(
                base64_authorization_header)
            base64_authorization_header = base64_authorization_header.decode(
                'utf-8')
        except binascii.Error:
            return None
        return base64_authorization_header

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        Extract user email and password from
        Base64 decoded Authorization header.

        Args:
        - decoded_base64_authorization_header (str):
        The decoded Base64 Authorization header.

        Returns:
        - Tuple[str, str]: The user email and password.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_password = decoded_base64_authorization_header.split(
            ':', 1)
        return user_email, user_password

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd: str) -> TypeVar('User'):
        """
        Get the User instance based on email and password.

        Args:
        - user_email (str): The user's email.
        - user_pwd (str): The user's password.

        Returns:
        - TypeVar('User'): The User instance.
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
