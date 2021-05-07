from flask import Blueprint

from app.blueprints.base import BaseResource
from app.blueprints.book.serializers import book_serializer
from app.blueprints.book.serializers import books_serializer
from app.blueprints.book.service import BookService
from app.blueprints.book.swagger import book_search_output_sw_model
from app.blueprints.book.swagger import book_sw_model
from app.decorators import token_required
from app.extensions import api as root_api

blueprint = Blueprint('books', __name__)
api = root_api.namespace('books', description='Books endpoints.')


class _BookBaseResource(BaseResource):
    book_service = BookService()


@api.route('')
class NewBookResource(_BookBaseResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(book_sw_model)
    @api.marshal_with(book_sw_model, envelope='data', code=201)
    @token_required
    def post(self) -> tuple:
        book = self.book_service.create(**self.request_payload())
        return book_serializer.dump(book), 201


@api.route('/<int:book_id>')
class BookResource(_BookBaseResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(book_sw_model, envelope='data')
    @token_required
    def get(self, book_id: int) -> tuple:
        book = self.book_service.find(book_id)
        return book_serializer.dump(book), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(book_sw_model)
    @api.marshal_with(book_sw_model, envelope='data')
    @token_required
    def put(self, book_id: int) -> tuple:
        book = self.book_service.save(book_id, **self.request_payload())
        return book_serializer.dump(book), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(book_sw_model, envelope='data')
    @token_required
    def delete(self, book_id: int) -> tuple:
        book = self.book_service.delete(book_id)
        return book_serializer.dump(book), 200


@api.route('/search')
class BooksSearchResource(_BookBaseResource):
    @api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(book_search_output_sw_model)
    @token_required
    def post(self) -> tuple:
        book_data = self.book_service.get(**self.request_payload())
        book_data_lst = list(book_data['query'].items)
        return {
            'data': books_serializer.dump(book_data_lst),
            'records_total': book_data['records_total'],
            'records_filtered': book_data['records_filtered'],
        }, 200
