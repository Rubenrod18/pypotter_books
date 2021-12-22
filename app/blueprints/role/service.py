from app.blueprints.base import BaseService
from app.blueprints.role import role_serializer
from app.blueprints.role import RoleManager
from app.extensions import db


class RoleService(BaseService):
    def __init__(self):
        super(RoleService, self).__init__()
        self.manager = RoleManager()
        self.serializer = role_serializer

    def create(self, **kwargs):
        serialized_data = self.serializer.load(kwargs)
        role = self.manager.create(**serialized_data)
        db.session.add(role)
        db.session.flush()
        return role

    def find_by_id(self, role_id: int, *args):
        self.serializer.load({'id': role_id}, partial=True)
        return self.manager.find_by_id(role_id)

    def save(self, role_id: int, **kwargs):
        serialized_data = self.serializer.load(kwargs)
        self.manager.save(role_id, **serialized_data)
        return self.manager.find_by_id(role_id)

    def delete(self, role_id: int):
        self.serializer.load({'id': role_id}, partial=True)
        role = self.manager.delete(role_id)
        db.session.flush()
        return role
