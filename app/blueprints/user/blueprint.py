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

blueprint = Blueprint('users', __name__)
_api = root_api.namespace(
    'users', description='Users with role admin can manage these endpoints.'
)


class _UserBaseResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(_UserBaseResource, self).__init__(*args, **kwargs)
        self._user_service = UserService()
        self._user_serializer = user_serializer
        self._users_serializer = users_serializer


@_api.route('')
class NewUserResource(_UserBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(user_input_sw_model)
    @_api.marshal_with(user_sw_model, envelope='data', code=201)
    @token_required
    @roles_accepted('admin')
    def post(self) -> tuple:
        user = self._user_service.create(self._request_payload())
        return self._user_serializer.dump(user), 201


@_api.route('/<int:user_id>')
class UserResource(_UserBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(user_sw_model, envelope='data')
    @token_required
    @roles_accepted('admin')
    def get(self, user_id: int) -> tuple:
        user = self._user_service.find(user_id)
        return self._user_serializer.dump(user), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(user_input_sw_model)
    @_api.marshal_with(user_sw_model, envelope='data')
    @token_required
    @roles_accepted('admin')
    def put(self, user_id: int) -> tuple:
        user = self._user_service.save(user_id, **self._request_payload())
        return self._user_serializer.dump(user), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(user_sw_model, envelope='data')
    @token_required
    @roles_accepted('admin')
    def delete(self, user_id: int) -> tuple:
        user = self._user_service.delete(user_id)
        return self._user_serializer.dump(user), 200


@_api.route('/search')
class UsersSearchResource(_UserBaseResource):
    @_api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    # TODO: Pending to define
    # @_api.expect(search_input_sw_model)
    @_api.marshal_with(user_search_output_sw_model)
    @token_required
    @roles_accepted('admin')
    def post(self) -> tuple:
        user_data = self._user_service.get(**self._request_payload())
        return {
            'data': self._users_serializer.dump(user_data['query'].items),
            'records_total': user_data['records_total'],
            'records_filtered': user_data['records_filtered'],
        }, 200
