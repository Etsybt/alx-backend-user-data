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
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ auth_header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        """
        return None
