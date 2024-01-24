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
        new_user = User(email=email, hashed_password=hashed_password)

        try:
            self._session.add(new_user)
            self._session.commit()
            return new_user
        except IntegrityError:
            # Handle IntegrityError, for example, if the email is not unique
            self._session.rollback()
            return None
