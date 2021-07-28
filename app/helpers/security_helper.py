import flask_security
from flask_security import hash_password
from flask_security import verify_password
from flask_security.passwordless import generate_login_token

from app.blueprints.user import User


class SecurityHelper:
    @staticmethod
    def create_token(user: User) -> str:
        return generate_login_token(user)

    @staticmethod
    def login_user(user: User) -> None:
        flask_security.login_user(user)

    @staticmethod
    def logout_user() -> None:
        flask_security.logout_user()

    @staticmethod
    def ensure_password(plain_password: str) -> str:
        return hash_password(plain_password)

    @staticmethod
    def match_password(plain_password: str, password_hash: str) -> bool:
        return verify_password(plain_password, password_hash)