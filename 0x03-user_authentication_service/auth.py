#!/usr/bin/env python3
"""
auth file
"""
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import bcrypt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """returns a salted hash of the input password
        """
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed

    def register_user(self, email: str, password: str) -> User:
        """registers a new user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return user
