from flask import Blueprint

from .serializers import shopping_cart_book_serializer
from .serializers import shopping_cart_books_serializer
from .service import ShoppingCartBookService
from .swagger import shopping_cart_book_search_output_sw_model
from .swagger import shopping_cart_book_sw_model
from app.blueprints.base import BaseResource
from app.blueprints.base import search_input_sw_model
from app.decorators import token_required
from app.extensions import api as root_api


blueprint = Blueprint('shopping_cart_books', __name__)
api = root_api.namespace(
    'shopping_cart_books', description='Shopping Cart Books endpoints.'
)


class _BaseShoppingCartBookResource(BaseResource):
    shopping_cart_book_service = ShoppingCartBookService()


@api.route('')
class NewShoppingCartBookResource(_BaseShoppingCartBookResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(shopping_cart_book_sw_model)
    @api.marshal_with(shopping_cart_book_sw_model, envelope='data', code=201)
    @token_required
    def post(self) -> tuple:
        book = self.shopping_cart_book_service.create(**self.request_payload())
        return shopping_cart_book_serializer.dump(book), 201


@api.route('/<int:shopping_cart_book_id>')
class ShoppingCartBookResource(_BaseShoppingCartBookResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(shopping_cart_book_sw_model, envelope='data')
    @token_required
    def get(self, shopping_cart_book_id: int) -> tuple:
        shopping_cart = self.shopping_cart_book_service.find(
            shopping_cart_book_id
        )
        return shopping_cart_book_serializer.dump(shopping_cart), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(shopping_cart_book_sw_model)
    @api.marshal_with(shopping_cart_book_sw_model, envelope='data')
    @token_required
    def put(self, shopping_cart_book_id: int) -> tuple:
        shopping_cart = self.shopping_cart_book_service.save(
            shopping_cart_book_id, **self.request_payload()
        )
        return shopping_cart_book_serializer.dump(shopping_cart), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(shopping_cart_book_sw_model, envelope='data')
    @token_required
    def delete(self, shopping_cart_book_id: int) -> tuple:
        book = self.shopping_cart_book_service.delete(shopping_cart_book_id)
        return shopping_cart_book_serializer.dump(book), 200


@api.route('/search')
class ShoppingCartBooksSearchResource(_BaseShoppingCartBookResource):
    @api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(search_input_sw_model)
    @api.marshal_with(shopping_cart_book_search_output_sw_model)
    @token_required
    def post(self) -> tuple:
        shopping_cart_data = self.shopping_cart_book_service.get(
            **self.request_payload()
        )
        shopping_cart_data_lst = list(shopping_cart_data['query'].items)
        return {
            'data': shopping_cart_books_serializer.dump(
                shopping_cart_data_lst
            ),
            'records_total': shopping_cart_data['records_total'],
            'records_filtered': shopping_cart_data['records_filtered'],
        }, 200
