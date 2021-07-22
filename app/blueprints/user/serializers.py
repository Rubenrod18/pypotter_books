import logging

from flask_security import hash_password
from marshmallow import fields
from marshmallow import post_dump
from marshmallow import post_load
from marshmallow import validate
from marshmallow import validates
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import NotFound

from .manager import User
from .manager import UserManager
from .models import Genre
from app.blueprints.role import RoleManager
from app.blueprints.role.serializers import RoleSerializer
from app.extensions import ma
from config import Config

logger = logging.getLogger(__name__)
user_manager = UserManager()
role_manager = RoleManager()


class _VerifyRoleId(fields.Field):
    def _deserialize(self, value, *args, **kwargs):
        role = role_manager.find(value)
        if role is None:
            raise NotFound(f'Role "{value}" not found')

        if role.deleted_at is not None:
            raise BadRequest(f'Role "{value}" deleted')
        return value


class UserSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = User
        ordered = True

    id = ma.auto_field()
    created_by = fields.Nested(lambda: UserSerializer(only=('id',)))
    name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    genre = ma.auto_field(validate=validate.OneOf(Genre.to_list()))
    birth_date = ma.auto_field()
    active = ma.auto_field()

    # Input fields
    password = ma.auto_field(
        validate=validate.Length(
            min=Config.SECURITY_PASSWORD_LENGTH_MIN, max=50
        ),
        load_only=True,
    )
    role_id = _VerifyRoleId(load_only=True)

    # Output fields
    created_at = ma.auto_field(dump_only=True, format='%Y-%m-%d %H:%M:%S')
    updated_at = ma.auto_field(dump_only=True, format='%Y-%m-%d %H:%M:%S')
    deleted_at = ma.auto_field(dump_only=True, format='%Y-%m-%d %H:%M:%S')
    roles = fields.List(
        fields.Nested(RoleSerializer, only=('name', 'label')), dump_only=True
    )

    @validates('id')
    def validate_id(self, user_id: int):
        kwargs = {'deleted_at': None}
        user = user_manager.find(user_id, **kwargs)

        if user is None:
            logger.debug(f'User "{user_id}" not found')
            raise NotFound('User not found')

        if user.deleted_at is not None:
            logger.debug(f'User "{user_id}" deleted')
            raise NotFound('User not found')

    @validates('email')
    def validate_email(self, email: str):
        if user_manager.find_by_email(email):
            raise BadRequest('User email already created')

    @post_load
    def post_load_process(self, data, **kwargs):
        if 'password' in data:
            data['password'] = hash_password(data['password'])

        if 'genre' in data:
            data['genre'] = Genre.deserialization(data['genre'])
        return data

    @post_dump
    def post_dump_process(self, data, **kwargs):
        if 'genre' in data:
            data['genre'] = Genre.serialization(data['genre'])
        return data


user_serializer = UserSerializer()
users_serializer = UserSerializer(many=True)
