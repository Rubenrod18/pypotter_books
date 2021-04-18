from datetime import datetime


class BaseManager(object):
    def __init__(self, *args, **kwargs):
        self.model = None

    @staticmethod
    def __order_by_clauses(db_model, payload) -> list:
        def build_order_by_column(field_name, sorting):
            field = getattr(db_model, field_name)
            return getattr(field, sorting)()

        default_order = [{'field_name': 'id', 'sorting': 'asc'}]
        payload_order = payload.get('order', default_order)
        db_columns = db_model.__table__.columns.keys()

        order_by = [
            build_order_by_column(item.get('field_name'), item.get('sorting'))
            for item in payload_order
            if item in db_columns
        ]

        return order_by

    @staticmethod
    def __search_conditions(db_model, payload) -> dict:
        filters = payload.get('search', {})
        sql_expressions = {}

        for item in filters:
            field_name = item['field_name']
            field_value = item['field_value']

            if (
                getattr(db_model, item['field_name'])
                and isinstance(field_value, str)
                and field_value.strip()
            ):
                sql_expressions.update({field_name: field_value})

        return sql_expressions

    def create(self, **kwargs):
        return self.model(**kwargs)

    def save(self, record_id: int, **kwargs):
        return self.model.query.filter_by(id=record_id).update(kwargs)

    def get(self, **kwargs):
        page = int(kwargs.get('page_number', 1))
        per_page = int(kwargs.get('items_per_page', 20))
        order_by = self.__order_by_clauses(self.model, kwargs)
        filters = self.__search_conditions(self.model, kwargs)

        query = (
            self.model.query.filter_by(**filters)
            .order_by(*order_by)
            .paginate(page, per_page)
        )

        return {
            'query': query,
            'records_total': len(self.model.query.all()),
            'records_filtered': len(query.items),
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
