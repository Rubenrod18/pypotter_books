from flask import Blueprint
from flask_security import roles_accepted

from .service import UserService
from app.blueprints.base import BaseResource
from app.blueprints.user import user_input_sw_model
from app.blueprints.user import user_search_output_sw_model
from app.blueprints.user import user_serializer
from app.blueprints.user import user_sw_model
from app.blueprints.user import users_serializer
from app.decorators import token_required
from app.extensions import api as root_api

_API_DESCRIPTION = (
    'Users with role admin or team_leader can manage these endpoints.'
)
blueprint = Blueprint('users', __name__)
api = root_api.namespace('users', description=_API_DESCRIPTION)


class UserBaseResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(BaseResource, self).__init__(*args, **kwargs)
        self.user_service = UserService()
        self.user_serializer = user_serializer
        self.users_serializer = users_serializer


@api.route('')
class NewUserResource(UserBaseResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(user_input_sw_model)
    @api.marshal_with(user_sw_model, envelope='data', code=201)
    @token_required
    @roles_accepted('admin')
    def post(self) -> tuple:
        user = self.user_service.create(self.request_payload())
        return self.user_serializer.dump(user), 201


@api.route('/<int:user_id>')
class UserResource(UserBaseResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(user_sw_model, envelope='data')
    @token_required
    @roles_accepted('admin')
    def get(self, user_id: int) -> tuple:
        user = self.user_service.find(user_id)
        return self.user_serializer.dump(user), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(user_input_sw_model)
    @api.marshal_with(user_sw_model, envelope='data')
    @token_required
    @roles_accepted('admin')
    def put(self, user_id: int) -> tuple:
        user = self.user_service.save(user_id, **self.request_payload())
        return self.user_serializer.dump(user), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(user_sw_model, envelope='data')
    @token_required
    @roles_accepted('admin')
    def delete(self, user_id: int) -> tuple:
        user = self.user_service.delete(user_id)
        return self.user_serializer.dump(user), 200


@api.route('/search')
class UsersSearchResource(UserBaseResource):
    @api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    # TODO: Pending to define
    # @api.expect(search_input_sw_model)
    @api.marshal_with(user_search_output_sw_model)
    @token_required
    @roles_accepted('admin')
    def post(self) -> tuple:
        user_data = self.user_service.get(**self.request_payload())
        return {
            'data': self.users_serializer.dump(user_data['query'].items),
            'records_total': user_data['records_total'],
            'records_filtered': user_data['records_filtered'],
        }, 200
