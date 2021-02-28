from app.blueprints.base import BaseManager


class BaseService(object):

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
        # TODO: pending to define
        # data = SearchSerializer().load(kwargs)
        return self.manager.get(**kwargs)

    def delete(self, record_id: int):
        return self.manager.delete(record_id)