#!/usr/bin/env python3
"""
auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage the API authentification
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ resuire_auth method
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ auth_header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        """
        return None
