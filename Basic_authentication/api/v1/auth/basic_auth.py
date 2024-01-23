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
