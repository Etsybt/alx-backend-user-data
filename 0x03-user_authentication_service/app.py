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


@app.route('/sessions', methods=['POST'])
def login_user() -> str:
    """logins the user and giving the seesion IDs
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_token = AUTH.create_session(email)

    response_data = {
        "email": email,
        "message": "logged in"
    }
    response = jsonify(response_data)

    response.set_cookie("session_token", session_token)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
