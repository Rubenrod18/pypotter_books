import flask_security
from flask_security.passwordless import generate_login_token

from .serializers import auth_user_login_serializer
from .swagger import auth_login_sw_model
from app.utils import filter_by_keys


class AuthService:
    @staticmethod
    def login_user(**kwargs) -> str:
        data = filter_by_keys(kwargs, auth_login_sw_model.keys())
        user = auth_user_login_serializer.load(data)

        token = generate_login_token(user)
        # TODO: Pending to testing whats happen if add a new field in user
        # model when a user is logged
        flask_security.login_user(user)
        return token

    @staticmethod
    def logout_user():
        flask_security.logout_user()
