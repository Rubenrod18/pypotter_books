from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.extensions import api


book_stock_sw_model = api.clone(
    'BookStock',
    record_monitoring_sw_model,
    {
        'book_id': fields.Integer(required=True),
        'country_id': fields.Integer(required=True),
        'quantity': fields.Integer(required=True),
    },
)

book_stock_search_output_sw_model = api.model(
    'BookStockSearchOutput',
    {
        'data': fields.List(fields.Nested(book_stock_sw_model)),
        'records_total': fields.Integer,
        'records_filtered': fields.Integer,
    },
)
