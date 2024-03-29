import logging

from flask import Blueprint
from flask_security import roles_required

from ...wrappers.cache_wrapper import CacheWrapper
from .serializers import role_serializer
from .serializers import roles_serializer
from .service import RoleService
from .swagger import role_input_sw_model
from .swagger import role_search_output_sw_model
from .swagger import role_sw_model
from app.blueprints.base import BaseResource
from app.blueprints.base import search_input_sw_model
from app.decorators import token_required
from app.extensions import api as root_api
from app.extensions import cache

logger = logging.getLogger(__name__)
blueprint = Blueprint('roles', __name__)
_api = root_api.namespace(
    'roles', description='Users with role admin can manage these endpoints.'
)


class _RoleBaseResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(_RoleBaseResource, self).__init__(*args, **kwargs)
        self._role_service = RoleService()


@_api.route('')
class NewListRolesResource(_RoleBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(role_input_sw_model)
    @_api.marshal_with(role_sw_model, envelope='data', code=201)
    @token_required
    @roles_required('admin')
    def post(self) -> tuple:
        role = self._role_service.create(**self._request_payload())
        return role_serializer.dump(role), 201

    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
        },
        security='auth_token',
    )
    @_api.marshal_with(role_sw_model, envelope='data', as_list=True)
    @token_required
    @roles_required('admin')
    @cache.cached(key_prefix=CacheWrapper.make_cache_key)
    def get(self) -> tuple:
        roles = self._role_service.all()
        return roles_serializer.dump(roles), 200


@_api.route('/<int:role_id>')
class RoleResource(_RoleBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not found',
        },
        security='auth_token',
    )
    @_api.marshal_with(role_sw_model, envelope='data')
    @token_required
    @roles_required('admin')
    @cache.cached(key_prefix=CacheWrapper.make_cache_key)
    def get(self, role_id: int) -> tuple:
        role = self._role_service.find_by_id(role_id)
        return role_serializer.dump(role), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(role_input_sw_model)
    @_api.marshal_with(role_sw_model, envelope='data')
    @token_required
    @roles_required('admin')
    def put(self, role_id: int) -> tuple:
        role = self._role_service.save(role_id, **self._request_payload())
        return role_serializer.dump(role), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
        },
        security='auth_token',
    )
    @_api.marshal_with(role_sw_model, envelope='data')
    @token_required
    @roles_required('admin')
    def delete(self, role_id: int) -> tuple:
        role = self._role_service.delete(role_id)
        return role_serializer.dump(role), 200


@_api.route('/search')
class RolesSearchResource(_RoleBaseResource):
    @_api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(search_input_sw_model)
    @_api.marshal_with(role_search_output_sw_model)
    @token_required
    @roles_required('admin')
    def post(self) -> tuple:
        role_data = self._role_service.get(**self._request_payload())
        return {
            'data': roles_serializer.dump(role_data['query'].items),
            'records_total': role_data['records_total'],
            'records_filtered': role_data['records_filtered'],
        }, 200
