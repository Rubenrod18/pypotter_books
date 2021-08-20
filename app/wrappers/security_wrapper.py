import typing

import flask_security
from flask_security import hash_password
from flask_security import verify_password
from flask_security.passwordless import generate_login_token
from flask_security.passwordless import login_token_status

if typing.TYPE_CHECKING:
    from app.blueprints.user import User


class SecurityWrapper:
    @staticmethod
    def create_token(user: 'User') -> str:
        return generate_login_token(user)

    @staticmethod
    def ensure_password(plain_password: str) -> str:
        return hash_password(plain_password)

    @staticmethod
    def login_user(user: 'User') -> None:
        flask_security.login_user(user)

    @staticmethod
    def logout_user() -> None:
        flask_security.logout_user()

    @staticmethod
    def login_token_status(token: str) -> tuple:
        return login_token_status(token)

    @staticmethod
    def match_password(plain_password: str, password_hash: str) -> bool:
        return verify_password(plain_password, password_hash)
