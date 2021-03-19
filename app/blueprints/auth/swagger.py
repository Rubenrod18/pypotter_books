from flask_restx import fields

from app.extensions import api

auth_login_sw_model = api.model('AuthUserLogin', {
    'email': fields.String(required=True),
    'password': fields.String(required=True),
})

auth_token_sw_model = api.model('AuthUserToken', {
    'token': fields.String()
})
