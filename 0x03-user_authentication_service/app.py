#!/usr/bin/env python3
"""
app file
"""
from flask import Flask, request, jsonify
from auth import Auth
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
AUTH = Auth()


@app.route('/users', methods=['POST'])
def users():
    """Register a new user."""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
