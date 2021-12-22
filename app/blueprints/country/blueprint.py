from flask import Blueprint

from app.blueprints.base import BaseResource
from app.blueprints.country.serializers import countries_serializer
from app.blueprints.country.serializers import country_serializer
from app.blueprints.country.service import CountryService
from app.blueprints.country.swagger import country_input_sw_model
from app.blueprints.country.swagger import country_search_output_sw_model
from app.blueprints.country.swagger import country_sw_model
from app.decorators import token_required
from app.extensions import api as root_api

blueprint = Blueprint('countries', __name__)
_api = root_api.namespace('countries', description='Countries endpoints.')


class _CountryBaseResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(
            _CountryBaseResource,
            self,
        ).__init__(*args, **kwargs)
        self._country_service = CountryService()


@_api.route('')
class NewCountryResource(_CountryBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(country_input_sw_model)
    @_api.marshal_with(country_sw_model, envelope='data', code=201)
    @token_required
    def post(self) -> tuple:
        country = self._country_service.create(**self._request_payload())
        return country_serializer.dump(country), 201


@_api.route('/<int:country_id>')
class CountryResource(_CountryBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(country_sw_model, envelope='data')
    @token_required
    def get(self, country_id: int) -> tuple:
        country = self._country_service.find(country_id)
        return country_serializer.dump(country), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(country_input_sw_model)
    @_api.marshal_with(country_sw_model, envelope='data')
    @token_required
    def put(self, country_id: int) -> tuple:
        country = self._country_service.save(
            country_id, **self._request_payload()
        )
        return country_serializer.dump(country), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(country_sw_model, envelope='data')
    @token_required
    def delete(self, country_id: int) -> tuple:
        country = self._country_service.delete(country_id)
        return country_serializer.dump(country), 200


@_api.route('/search')
class CountrysSearchResource(_CountryBaseResource):
    @_api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(country_search_output_sw_model)
    @token_required
    def post(self) -> tuple:
        country_data = self._country_service.get(**self._request_payload())
        country_data_lst = list(country_data['query'].items)
        return {
            'data': countries_serializer.dump(country_data_lst),
            'records_total': country_data['records_total'],
            'records_filtered': country_data['records_filtered'],
        }, 200
