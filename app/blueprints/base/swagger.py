from flask_restx import fields

from app.extensions import api

creator_sw_model = api.model('Creator', {
    'id': fields.Integer(readonly=True, example=3),
})

record_monitoring_sw_model = api.model('RecordMonitoring', {
    'id': fields.Integer(readonly=True, example=1),
    'created_at': fields.String(readonly=True, example='2000-01-01 00:00:00'),
    'updated_at': fields.String(readonly=True, example='2000-01-01 00:00:00'),
    'deleted_at': fields.String(readonly=True, example='2000-01-01 00:00:00'),
})
