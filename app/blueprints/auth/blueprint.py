from flask import Blueprint
from flask import request

from .swagger import auth_login_sw_model
from .swagger import auth_token_sw_model
from app.blueprints.base import BaseResource
from app.extensions import api as root_api
from app.services import AuthService
from app.utils.decorators import token_required

blueprint = Blueprint('auth', __name__)
api = root_api.namespace('auth', description='Authentication endpoints')


class AuthBaseResource(BaseResource):
    auth_service = AuthService()


@api.route('/login')
class AuthUserLoginResource(AuthBaseResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not found',
            422: 'Unprocessable Entity',
        },
    )
    @api.expect(auth_login_sw_model)
    @api.marshal_with(auth_token_sw_model)
    def post(self) -> tuple:
        token = self.auth_service.login_user(**request.get_json())
        return {'token': f'Bearer {token}'}, 200


@api.route('/logout')
class AuthUserLogoutResource(AuthBaseResource):
    @api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
        },
        security='auth_token',
    )
    @token_required
    def post(self) -> tuple:
        self.auth_service.logout_user()
        return {}, 204
