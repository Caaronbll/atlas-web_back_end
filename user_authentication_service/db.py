#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import IntegrityError


class DB:
    """DB class
    """
    total_users = 0
    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds a new user to the database """
        new_user = User(email = email, hashed_password = hashed_password)
        self.total_users += 1
        new_user.id = self.total_users
        new_user.session_id = str(self.total_users)
        new_user.reset_token = 'reset'

        session = self._session
        session.add(new_user)
        session.commit()

        return new_user
