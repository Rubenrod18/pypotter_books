from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.extensions import api


shopping_cart_book_sw_model = api.clone(
    'ShoppingCartBook',
    record_monitoring_sw_model,
    {
        'shopping_cart_id': fields.Integer(required=True),
        'book_id': fields.Integer(required=True),
        'discount': fields.Float(required=True),
    },
)

shopping_cart_book_search_output_sw_model = api.model(
    'ShoppingCartBookSearchOutput',
    {
        'data': fields.List(fields.Nested(shopping_cart_book_sw_model)),
        'records_total': fields.Integer,
        'records_filtered': fields.Integer,
    },
)
