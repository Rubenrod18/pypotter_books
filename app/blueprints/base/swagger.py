from flask_restx import fields

from app.extensions import api


class DictArbitrarySchema(fields.Raw):
    """

    TODO: fields.Raw doesn't allow show "readOnly: true" in Swagger UI.

    """

    def __init__(self, **kwargs):
        super(DictArbitrarySchema, self).__init__(**kwargs)
        self.description = 'Structure with arbitrary schema'

    def output(self, key, obj, *args, **kwargs):
        dct = {}

        try:
            if isinstance(obj, dict):
                dct = obj.get(key)
        except AttributeError:
            dct = {}

        return dct or {}


creator_sw_model = api.model(
    'Creator',
    {
        'id': fields.Integer(readonly=True, example=3),
    },
)

record_monitoring_sw_model = api.model(
    'RecordMonitoring',
    {
        'id': fields.Integer(readonly=True, example=1),
        'created_at': fields.String(
            readonly=True, example='2000-01-01 00:00:00'
        ),
        'updated_at': fields.String(
            readonly=True, example='2000-01-01 00:00:00'
        ),
        'deleted_at': fields.String(
            readonly=True, example='2000-01-01 00:00:00'
        ),
        '_links': DictArbitrarySchema(
            readonly=True,
            example='{"link1": "/api/records", "link2": "/api/record/1"}',  # noqa
        ),
    },
)

_search_fields_input_sw_model = api.model(
    'SearchFields',
    {
        'field_name': fields.String(required=True, example='name'),
        'field_value': fields.String(
            required=True,
            description='Could be string or integer.',
            example='Guido van Rossum',
        ),
    },
)

_search_order_input_sw_model = api.model(
    'SearchOrderInput',
    {
        'field_name': fields.String(required=True),
        'sorting': fields.String(required=True, enum=['asc', 'desc']),
    },
)

_order_description = (
    'First value is the field name, second value is the '
    'sort ( asc or desc ).'
)

search_input_sw_model = api.model(
    'SearchInput',
    {
        'search': fields.List(
            fields.Nested(_search_fields_input_sw_model, required=True)
        ),
        'order': fields.List(
            fields.Nested(
                _search_order_input_sw_model,
                description=_order_description,
                required=True,
            ),
            example=[
                {'field_name': 'name', 'sorting': 'asc'},
                {'field_name': 'created_at', 'sorting': 'desc'},
            ],
        ),
        'items_per_page': fields.Integer(required=True, example=10),
        'page_number': fields.Integer(required=True, example=1),
    },
)
