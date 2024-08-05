#!/usr/bin/env python3
"""
basic_auth
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic authentication class
    """
    def extract_base64_authorization_header(
            self,  authorization_header: str) -> str:
        """ Extract Base64 part of the Authorization
        header for Basic Authentication
        """
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode Base64 authorization header
        """
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (TypeError, ValueError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user email and password from the decoded Base64 string
        """
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
