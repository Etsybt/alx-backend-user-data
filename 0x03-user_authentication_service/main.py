#!/usr/bin/env python3
"""
main file
"""
import requests

BASE_URL = 'http://localhost:5000'
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Test user registration"""
    response = requests.post(f'{BASE_URL}/users', data={
        "email": email,
        "password": password
    })

    expected_response = {"email": email, "message": "user created"}

    assert response.status_code == 200
    assert response.json() == expected_response


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login with incorrect password"""
    response = requests.post(f'{BASE_URL}/sessions', data={
        "email": email,
        "password": password
    })

    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test successful login and return session_id"""
    response = requests.post(f'{BASE_URL}/sessions', data={
        "email": email,
        "password": password
    })

    expected_response = {"email": email, "message": "logged in"}

    assert response.status_code == 200
    assert response.json() == expected_response

    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """Test profile access without login"""
    response = requests.get(f'{BASE_URL}/profile', cookies={
        "session_id": ""
    })

    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test profile access with valid session_id"""
    response = requests.get(f'{BASE_URL}/profile', cookies={
        "session_id": session_id
    })

    expected_response = {"email": EMAIL}

    assert response.status_code == 200
    assert response.json() == expected_response


def log_out(session_id: str) -> None:
    """Test logout functionality"""
    response = requests.delete(f'{BASE_URL}/sessions', cookies={
        "session_id": session_id
    })

    expected_response = {"message": "Bienvenue"}

    assert response.status_code == 200
    assert response.json() == expected_response


def reset_password_token(email: str) -> str:
    """Request a password reset token"""
    response = requests.post(f'{BASE_URL}/reset_password', data={
        "email": email
    })

    assert response.status_code == 200

    response_json = response.json()
    reset_token = response_json.get("reset_token")

    expected_response = {"email": email, "reset_token": reset_token}

    assert response_json == expected_response

    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update the password using a reset token"""
    response = requests.put(f'{BASE_URL}/reset_password', data={
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    })

    expected_response = {"email": email, "message": "Password updated"}

    assert response.status_code == 200
    assert response.json() == expected_response


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
