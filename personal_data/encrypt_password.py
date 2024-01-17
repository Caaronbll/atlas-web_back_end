#!/usr/bin/env python3
"""
Task 6 - Check valid password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Generate a salted, hashed password using bcrypt."""
    password_bytes = password.encode('utf-8')

    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate that the provided password matches the hashed password."""
    password_bytes = password.encode('utf-8')

    return bcrypt.checkpw(password_bytes, hashed_password)