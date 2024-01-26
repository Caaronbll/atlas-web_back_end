#!/usr/bin/env python3
"""
Task 4 - Auth class
"""
from db import DB
import bcrypt
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Hashes a password """
    salt = bcrypt.gensalt()
    encodedpw = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(encodedpw, salt)
    return hashed_password


def _generate_uuid() -> str:
    """ Generates a new uuid """
    return str(uuid.uuid4())


class Auth(DB):
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user to the database """
        try:
            if self._db.find_user_by(email=email):
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ validating credentials for login """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Retruns session ID based on email """
        user = self._db.find_user_by(email=email)
        user.session_id = _generate_uuid()
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Returns user from session ID """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroys a session based on user ID """
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Returns the reset password token """
        user = self._db.find_user_by(email=email)
        if user is None:
            raise ValueError
        elif user:
            new_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=new_token)
        return new_token
