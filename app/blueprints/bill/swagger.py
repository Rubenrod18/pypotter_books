from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.extensions import api


bill_sw_model = api.clone(
    'Bill',
    record_monitoring_sw_model,
    {
        'user_id': fields.Integer(required=True),
        'currency_id': fields.Integer(required=True),
        'shopping_cart_id': fields.Integer(required=True),
    },
)

bill_search_output_sw_model = api.model(
    'BillSearchOutput',
    {
        'data': fields.List(fields.Nested(bill_sw_model)),
        'records_total': fields.Integer,
        'records_filtered': fields.Integer,
    },
)
