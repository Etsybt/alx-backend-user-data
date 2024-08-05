#!/usr/bin/env python3
"""
basic_auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic authentication class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Extract Base64 part of the Authorization header for Basic Authentication
        """
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
