import logging

from flask_security import verify_password
from marshmallow import fields
from marshmallow import post_load
from marshmallow import validate
from marshmallow import validates
from werkzeug.exceptions import Unauthorized

from app.blueprints.user import UserManager
from app.extensions import ma
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
    __user = None

    @validates('email')
    def validate_email(self, email):
        kwargs = {'active': True, 'deleted_at': None}
        self.__user = user_manager.find_by_email(email, **kwargs)

        if self.__user is None:
            logger.debug(f'User "{email}" not found.')
            raise Unauthorized('Credentials invalid')

        if self.__user.active is False:
            logger.debug(f'User "{email}" not activated.')
            raise Unauthorized('Credentials invalid')

        if self.__user.deleted_at is not None:
            logger.debug(f'User "{email}" deleted.')
            raise Unauthorized('Credentials invalid')

    @validates('password')
    def validate_password(self, password):
        if not verify_password(password, self.__user.password):
            logger.debug(
                f'User "{self.__user.email}" password ' f'does not match.'
            )
            raise Unauthorized('Credentials invalid')

    @post_load
    def make_object(self, data, **kwargs):
        return self.__user


auth_user_login_serializer = AuthUserLoginSerializer()
