#!/usr/bin/env python3
"""
Task 6 - Check valid password
"""
import bcrypt


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate that the provided password matches the hashed password."""
    password_bytes = password.encode('utf-8')

    return bcrypt.checkpw(password_bytes, hashed_password)