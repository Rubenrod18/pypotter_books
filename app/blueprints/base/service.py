from app.blueprints.base import BaseManager
from app.blueprints.base.serializers import search_serializer


class BaseService:
    def __init__(self, *args, **kwargs):
        self.manager = BaseManager()

    def create(self, **kwargs):
        return self.manager.create(**kwargs)

    def find(self, record_id: int, *args):
        return self.manager.find(record_id, *args)

    def save(self, record_id: int, **kwargs):
        self.manager.save(record_id, **kwargs)
        return self.manager.find(record_id, **{'deleted_at': None})

    def get(self, **kwargs):
        serialized_data = search_serializer.load(kwargs)
        return self.manager.get(**serialized_data)

    def delete(self, record_id: int):
        return self.manager.delete(record_id)
