from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.extensions import api


currency_sw_model = api.clone(
    'Currency',
    record_monitoring_sw_model,
    {
        'code': fields.String(required=True),
        'decimals': fields.Integer(),
        'name': fields.String(required=True),
        'name_plural': fields.String(required=True),
        'num': fields.String(required=True),
        'symbol': fields.String(required=True),
        'symbol_native': fields.String(required=True),
    },
)

currency_search_output_sw_model = api.model(
    'CurrencySearchOutput',
    {
        'data': fields.List(fields.Nested(currency_sw_model)),
        'records_total': fields.Integer,
        'records_filtered': fields.Integer,
    },
)
