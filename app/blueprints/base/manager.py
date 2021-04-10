from datetime import datetime


class BaseManager(object):
    def __init__(self, *args, **kwargs):
        self.model = None

    def create(self, **kwargs):
        return self.model(**kwargs)

    def save(self, record_id: int, **kwargs):
        return self.model.query.filter_by(id=record_id).update(kwargs)

    def get(self, **kwargs):
        # TODO: pending to define search
        query = self.model.query.all()
        records_total = len(query)

        return {
            'query': query,
            'records_total': len(query),
            'records_filtered': records_total,
        }

    def delete(self, record_id: int):
        record = self.find(record_id)
        record.deleted_at = datetime.utcnow()
        return record

    def find(self, record_id: int, **kwargs):
        query = {'id': record_id}
        if kwargs:
            query.update(kwargs)
        return self.model.query.filter_by(**query).first()

    def raw(self, query: str):
        return self.model.raw(query)
