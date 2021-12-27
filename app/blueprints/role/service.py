from app.blueprints.base import BaseService
from app.blueprints.role import role_serializer
from app.blueprints.role import RoleManager
from app.extensions import db
from app.wrappers.cache_wrapper import CacheWrapper


class RoleService(BaseService):
    def __init__(self):
        super(RoleService, self).__init__()
        self.manager = RoleManager()
        self.serializer = role_serializer

    def all(self):
        return self.manager.all()

    def create(self, **kwargs):
        deserialized_data = self.serializer.load(kwargs)
        role = self.manager.create(**deserialized_data)
        db.session.add(role)
        db.session.flush()
        CacheWrapper.delete('get/api/roles')
        return role

    def find_by_id(self, role_id: int, *args):
        self.serializer.load({'id': role_id}, partial=True)
        return self.manager.find_by_id(role_id)

    def save(self, role_id: int, **kwargs):
        deserialized_data = self.serializer.load(kwargs)
        self.manager.save(role_id, **deserialized_data)
        CacheWrapper.delete('get/api/roles', f'get/api/roles/{role_id}')
        return self.manager.find_by_id(role_id)

    def delete(self, role_id: int):
        self.serializer.load({'id': role_id}, partial=True)
        role = self.manager.delete(role_id)
        db.session.flush()
        CacheWrapper.delete('get/api/roles', f'get/api/roles/{role_id}')
        return role
