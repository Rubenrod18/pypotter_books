from app.blueprints.role import role_serializer
from app.blueprints.role import RoleManager
from app.extensions import db
from app.services.base_service import BaseService


class RoleService(BaseService):
    def __init__(self):
        super(RoleService, self).__init__()
        self.manager = RoleManager()
        self.serializer = role_serializer

    def create(self, **kwargs):
        serialized_data = self.serializer.load(kwargs)
        role = self.manager.create(**serialized_data)
        db.session.add(role)
        db.session.commit()
        return role

    def find(self, role_id: int, *args):
        self.serializer.load({'id': role_id}, partial=True)
        return self.manager.find(role_id)

    def save(self, role_id: int, **kwargs):
        serialized_data = self.serializer.load(kwargs)
        self.manager.save(role_id, **serialized_data)
        db.session.commit()
        return self.manager.find(role_id)

    def delete(self, role_id: int):
        self.serializer.load({'id': role_id}, partial=True)
        role = self.manager.delete(role_id)
        db.session.commit()
        return role
