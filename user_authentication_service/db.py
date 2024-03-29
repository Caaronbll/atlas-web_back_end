#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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

    def find_user_by(self, **kwargs) -> User:
        """ Returns the first row found in the users table """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except (InvalidRequestError, NoResultFound) as e:
            raise e

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update a user's attributes based on user_id """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if hasattr(User, key):
                setattr(User, key, value)
            else:
                raise ValueError(f"Invalid attribute: {key}")
        self._session.commit()
