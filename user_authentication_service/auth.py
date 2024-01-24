#!/usr/bin/env python3
"""
Task 4 - Auth class
"""
from db import DB
import bcrypt
from user import User

def _hash_password(password: str) -> bytes:
    """ Hashes a password """
    salt = bcrypt.gensalt()
    encodedpw = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(encodedpw, salt)
    return hashed_password


class Auth(DB):
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user to the database """
        if self._db.find_user_by(email=email):
            raise ValueError(f"User <user's email> already exists")
        else:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
        return user
