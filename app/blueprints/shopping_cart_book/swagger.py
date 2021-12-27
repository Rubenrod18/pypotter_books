from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.extensions import api


shopping_cart_book_sw_model = api.clone(
    'ShoppingCartBook',
    record_monitoring_sw_model,
    {
        'shopping_cart_id': fields.Integer(required=True),
        'book_id': fields.Integer(required=True),
        'units': fields.Integer(required=True),
    },
)

shopping_cart_book_input_sw_model = api.model(
    'ShoppingCartBookInput',
    {
        'shopping_cart_id': fields.Integer(required=True),
        'book_ids': fields.List(fields.Integer(required=True), required=True),
        'units': fields.List(fields.Integer(required=True), required=True),
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
