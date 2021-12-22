import logging
import typing
from datetime import datetime

from app.exceptions import DoesNotExist
from app.helpers import StrHelper

if typing.TYPE_CHECKING:
    from flask_sqlalchemy import BaseQuery


logger = logging.getLogger(__name__)


class BaseManager:
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

            if isinstance(field_value, str):
                field_value = field_value.strip()

            if getattr(db_model, item['field_name']) and (
                isinstance(field_value, str)
                or isinstance(field_value, int)
                or isinstance(field_value, float)
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
        record = self.find_by_id(record_id)
        record.deleted_at = datetime.utcnow()
        return record

    def find(self, *args, **kwargs) -> 'BaseQuery':
        base_query = self.find_or_none(*args, **kwargs)

        if base_query is None:
            logger.exception(
                f'Model "{self.model.__name__}" not found. '
                f'Params: {args} - {kwargs}'
            )
            model_name = StrHelper.pascal_case_to_normal_case(
                self.model.__name__
            ).title()
            raise DoesNotExist(description=f'{model_name} not found')

        return base_query

    def find_by_id(self, record_id: int, **kwargs) -> 'BaseQuery':
        query = {'id': record_id}

        if kwargs:
            query.update(kwargs)

        return self.find(**query)

    def find_or_none(self, *args, **kwargs) -> 'BaseQuery':
        base_query = self.model.query.filter()

        if args:
            base_query = base_query.filter(*args)

        return base_query.filter_by(**kwargs).first()

    def raw(self, query: str):
        return self.model.raw(query)
