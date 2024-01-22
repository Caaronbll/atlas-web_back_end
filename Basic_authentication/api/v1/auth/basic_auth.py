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
        if authorization_header is not type(str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        base64_part = authorization_header.split("Basic ")[1].strip()
        return base64_part