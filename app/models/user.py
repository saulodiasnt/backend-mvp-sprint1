import datetime
from app.database import db
import bcrypt


class User(db.Model):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        created_at (datetime): The timestamp when the user was created.
        updated_at (datetime): The timestamp when the user was last updated.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    def set_password(self, password):
        """
        Sets the password for the user.

        Parameters:
        - password (str): The password to be set.

        Returns:
        None
        """
        self.password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, password):
        """
        Check if the provided password matches the user's stored password.

        Parameters:
        - password (str): The password to be checked.

        Returns:
        - bool: True if the password matches, False otherwise.
        """
        try:
            return bcrypt.checkpw(
                password.encode("utf-8"), self.password.encode("utf-8")
            )
        except Exception as e:
            print(e)
            return False

    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        """
        Returns a dictionary representation of the user.

        Returns:
        - dict: A dictionary representation of the user.
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
