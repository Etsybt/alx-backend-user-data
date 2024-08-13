#!/usr/bin/env python3
"""
auth file
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """returns a salted hash of the input password
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
