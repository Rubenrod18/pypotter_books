from flask import Blueprint

from .serializers import book_price_serializer
from .serializers import book_prices_serializer
from .service import BookPriceService
from .swagger import book_price_search_output_sw_model
from .swagger import book_price_sw_model
from app.blueprints.base import BaseResource
from app.decorators import token_required
from app.extensions import api as root_api

blueprint = Blueprint('book_prices', __name__)
api = root_api.namespace('book_prices', description='Book Prices endpoints.')


class _BookPriceBaseResource(BaseResource):
    book_price_service = BookPriceService()


@api.route('')
class NewBookPriceResource(_BookPriceBaseResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(book_price_sw_model)
    @api.marshal_with(book_price_sw_model, envelope='data', code=201)
    @token_required
    def post(self) -> tuple:
        book_price = self.book_price_service.create(**self.request_payload())
        return book_price_serializer.dump(book_price), 201


@api.route('/<int:book_id>')
class BookPriceResource(_BookPriceBaseResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(book_price_sw_model, envelope='data')
    @token_required
    def get(self, book_id: int) -> tuple:
        book_price = self.book_price_service.find(book_id)
        return book_price_serializer.dump(book_price), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(book_price_sw_model)
    @api.marshal_with(book_price_sw_model, envelope='data')
    @token_required
    def put(self, book_id: int) -> tuple:
        book_price = self.book_price_service.save(
            book_id, **self.request_payload()
        )
        return book_price_serializer.dump(book_price), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(book_price_sw_model, envelope='data')
    @token_required
    def delete(self, book_id: int) -> tuple:
        book_price = self.book_price_service.delete(book_id)
        return book_price_serializer.dump(book_price), 200


@api.route('/search')
class BookPricesSearchResource(_BookPriceBaseResource):
    @api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(book_price_search_output_sw_model)
    @token_required
    def post(self) -> tuple:
        book_price_data = self.book_price_service.get(**self.request_payload())
        book_price_data_lst = list(book_price_data['query'].items)

        return {
            'data': book_prices_serializer.dump(book_price_data_lst),
            'records_total': book_price_data['records_total'],
            'records_filtered': book_price_data['records_filtered'],
        }, 200
