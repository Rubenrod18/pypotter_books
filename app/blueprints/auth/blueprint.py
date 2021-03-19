from flask import Blueprint, request
from flask_restx import Resource

from app.extensions import api as root_api
from app.services import AuthService
from app.utils.decorators import token_required
from .swagger import auth_login_sw_model, auth_token_sw_model

blueprint = Blueprint('auth', __name__)
api = root_api.namespace('auth', description='Authentication endpoints')


class AuthBaseResource(Resource):
    auth_service = AuthService()


@api.route('/login')
class AuthUserLoginResource(AuthBaseResource):
    @api.doc(responses={401: 'Unauthorized', 403: 'Forbidden',
                        404: 'Not found', 422: 'Unprocessable Entity'})
    @api.expect(auth_login_sw_model)
    @api.marshal_with(auth_token_sw_model)
    def post(self) -> tuple:
        token = self.auth_service.login_user(**request.get_json())
        return {'token': f'Bearer {token}'}, 200


@api.route('/logout')
class AuthUserLogoutResource(AuthBaseResource):
    @api.doc(responses={200: 'Success', 401: 'Unauthorized'},
             security='auth_token')
    @token_required
    def post(self) -> tuple:
        self.auth_service.logout_user()
        return {}, 204