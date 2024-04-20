from flask import jsonify
from datetime import timedelta
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.database import db
from app.shared.erros import UnauthorizedException


class AuthService:
    """
    Service class for handling authentication-related operations.
    """

    @staticmethod
    def login(email: str, password: str):
        """
        Authenticates a user by checking the provided email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            dict: A dictionary containing the access token and user information.

        Raises:
            Exception: If the email or password is invalid.
        """
        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
            return UnauthorizedException("Invalid email or password.").to_dict()
        expire_delta = timedelta(days=1)
        access_token = create_access_token(identity=user.id, expires_delta=expire_delta)

        return jsonify(access_token=access_token, user=user.to_dict())

    @staticmethod
    def register(name: str, email: str, password: str):
        """
        Register a new user.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            dict: A dictionary containing the user information.

        """
        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict())
