#!/usr/bin/env python3
"""
Task 4 - Auth class
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashes a password """
    salt = bcrypt.gensalt()
    encodedpw = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(encodedpw, salt)
    return hashed_password


class Auth():
    """ Auth Class """