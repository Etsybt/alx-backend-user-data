#!/usr/bin/env python3
"""
a simple Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> str:
    """registers a new user
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"})


@app.route("/sessions", methods=["POST"])
def login() -> str:
    """logins the user
    """
    try:
        user_email = request.form['email']
        user_password = request.form['password']
    except KeyError:
        abort(400)

    if not authentication_service.is_valid_login(user_email, user_password):
        abort(401)

    session_token = authentication_service.create_session(user_email)

    response_data = {
        "email": user_email,
        "message": "Logged in successfully"
    }
    response = jsonify(response_data)

    response.set_cookie("session_token", session_token)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
