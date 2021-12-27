from flask import Blueprint

from .serializers import book_price_serializer
from .serializers import book_prices_serializer
from .swagger import book_price_search_output_sw_model
from .swagger import book_price_sw_model
from app.blueprints.base import BaseResource
from app.blueprints.book_price.services.book_price_service import (
    BookPriceService,
)
from app.decorators import token_required
from app.extensions import api as root_api

blueprint = Blueprint('book_prices', __name__)
_api = root_api.namespace('book_prices', description='Book Prices endpoints.')


class _BookPriceBaseResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(_BookPriceBaseResource, self).__init__(*args, **kwargs)
        self._book_price_service = BookPriceService()


@_api.route('')
class NewBookPriceResource(_BookPriceBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(book_price_sw_model)
    @_api.marshal_with(book_price_sw_model, envelope='data', code=201)
    @token_required
    def post(self) -> tuple:
        book_price = self._book_price_service.create(**self._request_payload())
        return book_price_serializer.dump(book_price), 201


@_api.route('/<int:book_id>')
class BookPriceResource(_BookPriceBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(book_price_sw_model, envelope='data')
    @token_required
    def get(self, book_id: int) -> tuple:
        book_price = self._book_price_service.find_by_id(book_id)
        return book_price_serializer.dump(book_price), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(book_price_sw_model)
    @_api.marshal_with(book_price_sw_model, envelope='data')
    @token_required
    def put(self, book_id: int) -> tuple:
        book_price = self._book_price_service.save(
            book_id, **self._request_payload()
        )
        return book_price_serializer.dump(book_price), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(book_price_sw_model, envelope='data')
    @token_required
    def delete(self, book_id: int) -> tuple:
        book_price = self._book_price_service.delete(book_id)
        return book_price_serializer.dump(book_price), 200


@_api.route('/search')
class BookPricesSearchResource(_BookPriceBaseResource):
    @_api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(book_price_search_output_sw_model)
    @token_required
    def post(self) -> tuple:
        book_price_data = self._book_price_service.get(
            **self._request_payload()
        )
        book_price_data_lst = list(book_price_data['query'].items)

        return {
            'data': book_prices_serializer.dump(book_price_data_lst),
            'records_total': book_price_data['records_total'],
            'records_filtered': book_price_data['records_filtered'],
        }, 200
