from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.extensions import api


shopping_cart_sw_model = api.clone(
    'ShoppingCart',
    record_monitoring_sw_model,
    {
        'user_id': fields.Integer(required=True),
    },
)

shopping_cart_search_output_sw_model = api.model(
    'ShoppingCartSearchOutput',
    {
        'data': fields.List(fields.Nested(shopping_cart_sw_model)),
        'records_total': fields.Integer,
        'records_filtered': fields.Integer,
    },
)
