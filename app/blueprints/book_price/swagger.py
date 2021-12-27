from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.extensions import api


book_price_sw_model = api.clone(
    'BookPrice',
    record_monitoring_sw_model,
    {
        'book_id': fields.Integer(required=True),
        'country_id': fields.Integer(required=True),
        'price': fields.Float(required=True),
    },
)

book_price_search_output_sw_model = api.model(
    'BookPriceSearchOutput',
    {
        'data': fields.List(fields.Nested(book_price_sw_model)),
        'records_total': fields.Integer,
        'records_filtered': fields.Integer,
    },
)
