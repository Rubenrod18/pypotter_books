import logging

from marshmallow import fields
from marshmallow import post_load
from marshmallow import validate
from werkzeug.exceptions import Unauthorized

from app.blueprints.user import User
from app.blueprints.user import UserManager
from app.extensions import ma
from app.wrappers import SecurityWrapper
from config import Config

logger = logging.getLogger(__name__)
user_manager = UserManager()


class AuthUserLoginSerializer(ma.Schema):
    email = fields.Str(load_only=True, required=True)
    password = fields.Str(
        load_only=True,
        required=True,
        validate=validate.Length(
            min=Config.SECURITY_PASSWORD_LENGTH_MIN, max=50
        ),
    )

    @staticmethod
    def __check_password(user: User, plain_password: str) -> None:
        if not SecurityWrapper.match_password(plain_password, user.password):
            logger.debug(f'User "{user.email}" password does not match.')
            raise Unauthorized('Credentials invalid')

    @staticmethod
    def __find_user(email: str) -> User:
        user = user_manager.find_by_email(email)

        if user is None:
            logger.debug(f'User "{email}" not found.')
            raise Unauthorized('User not found')

        if user.active is False:
            logger.debug(f'User "{email}" is not activated.')
            raise Unauthorized('User is not activated')

        if user.deleted_at is not None:
            logger.debug(f'User "{email}" is deleted.')
            raise Unauthorized('User is deleted')

        return user

    @post_load
    def make_object(self, data, **kwargs):  # noqa
        user = self.__find_user(data['email'])
        self.__check_password(user, data['password'])
        return user


auth_user_login_serializer = AuthUserLoginSerializer()
