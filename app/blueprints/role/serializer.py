import logging

from marshmallow import post_load, validates
from werkzeug.exceptions import BadRequest, NotFound

from app.blueprints.base import TimestampField
from app.extensions import ma
from .manager import RoleModel, RoleManager

logger = logging.getLogger(__name__)
role_manager = RoleManager()


class RoleSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = RoleModel
        ordered = True

    id = ma.auto_field()
    name = ma.auto_field(dump_only=True)
    description = ma.auto_field()
    label = ma.auto_field()
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)

    @validates('id')
    def validate_id(self, role_id):
        kwargs = {'deleted_at': None}
        role = role_manager.find(role_id, **kwargs)

        if role is None:
            logger.debug(f'Role "{role_id}" not found.')
            raise NotFound('Role not found')

        if role.deleted_at is not None:
            logger.debug(f'Role "{role_id}" already deleted.')
            raise NotFound('Role not found')

    @post_load
    def sluglify_name(self, item, many, **kwargs):
        if item.get('label'):
            item['name'] = item['label'].lower().strip().replace(' ', '-')
        return item

    @validates('name')
    def validate_name(self, value, **kwargs):
        if role_manager.model.get_or_none(name=value):
            raise BadRequest('Role name already created')


role_serializer = RoleSerializer()
roles_serializer = RoleSerializer(many=True)
