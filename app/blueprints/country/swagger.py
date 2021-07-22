from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.blueprints.currency.swagger import currency_sw_model
from app.extensions import api


country_sw_model = api.clone(
    'Country',
    record_monitoring_sw_model,
    {
        'name': fields.String(required=True),
        'alpha_2_code': fields.String(required=True),
        'alpha_3_code': fields.String(required=True),
        'currency': fields.Nested(currency_sw_model),
    },
)

country_input_sw_model = api.clone(
    'CountryInput',
    {
        'name': fields.String(required=True),
        'alpha_2_code': fields.String(required=True),
        'alpha_3_code': fields.String(required=True),
        'currency_id': fields.Integer(required=True),
    },
)

country_search_output_sw_model = api.model(
    'CountrySearchOutput',
    {
        'data': fields.List(fields.Nested(country_sw_model)),
        'records_total': fields.Integer,
        'records_filtered': fields.Integer,
    },
)
