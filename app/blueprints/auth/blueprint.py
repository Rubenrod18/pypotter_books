from flask import Blueprint

from . import auth_user_login_serializer
from .swagger import auth_login_sw_model
from .swagger import auth_token_sw_model
from app.blueprints.base import BaseResource
from app.decorators import token_required
from app.extensions import api as root_api
from app.helpers import SecurityHelper

blueprint = Blueprint('auth', __name__)
api = root_api.namespace('auth', description='Authentication endpoints.')


class AuthBaseResource(BaseResource):
    pass


@api.route('/login')
class AuthUserLoginResource(AuthBaseResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            422: 'Unprocessable Entity',
        },
    )
    @api.expect(auth_login_sw_model)
    @api.marshal_with(auth_token_sw_model)
    def post(self) -> tuple:
        user = auth_user_login_serializer.load(self.request_payload())
        # TODO: Pending to testing whats happen if add a new field in user
        # model when a user is logged
        SecurityHelper.login_user(user)
        token = SecurityHelper.create_token(user)
        return {'token': f'Bearer {token}'}, 200


@api.route('/logout')
class AuthUserLogoutResource(AuthBaseResource):
    @api.doc(
        responses={
            204: 'No Content',
            403: 'Forbidden',
            401: 'Unauthorized',
        },
        security='auth_token',
    )
    @token_required
    def post(self) -> tuple:
        SecurityHelper.logout_user()
        return {}, 204
