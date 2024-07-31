#!/usr/bin/env python3
"""
encrypt_password
"""
import bcrypt


def hash_password(password):
    """
    Hashes a password using the bcrypt package.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password, password):
    """
    Validates if the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The salted, hashed password.
        password (str): The password to be validated.

    Returns:
        bool: True if the password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
