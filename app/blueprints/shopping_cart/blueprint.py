from flask import Blueprint

from ...wrappers import SecurityWrapper
from ..book_price.services.book_price_service import BookPriceService
from ..shopping_cart_book.service import ShoppingCartBookService
from .serializers import shopping_cart_serializer
from .serializers import shopping_carts_serializer
from .service import ShoppingCartService
from .swagger import shopping_cart_input_sw_model
from .swagger import shopping_cart_search_output_sw_model
from .swagger import shopping_cart_sw_model
from app.blueprints.base import BaseResource
from app.decorators import token_required
from app.extensions import api as root_api

blueprint = Blueprint('shopping_carts', __name__)
_api = root_api.namespace(
    'shopping_carts', description='Shopping carts endpoints.'
)


class _ShoppingCartResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(_ShoppingCartResource, self).__init__(*args, **kwargs)
        self._book_price_service = BookPriceService()
        self._shopping_cart_service = ShoppingCartService()
        self._shopping_cart_book_service = ShoppingCartBookService()


@_api.route('')
class NewShoppingCartResource(_ShoppingCartResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(shopping_cart_input_sw_model)
    @_api.marshal_with(shopping_cart_sw_model, envelope='data', code=201)
    @token_required
    def post(self) -> tuple:
        current_user = SecurityWrapper.current_user()
        shopping_cart = self._shopping_cart_service.create(
            **{'user_id': current_user.id, 'total_price': 0}
        )

        request_payload = self._request_payload()
        request_payload['shopping_cart_id'] = shopping_cart.id
        shopping_cart_books = self._shopping_cart_book_service.create(
            **request_payload
        )

        book_ids = []
        for shopping_cart_book in shopping_cart_books:
            book_ids += [shopping_cart_book.book_id] * shopping_cart_book.units

        self._shopping_cart_service.manager.save(
            shopping_cart.id,
            **{'total_price': self._book_price_service.cal_price(book_ids)}
        )
        return shopping_cart_serializer.dump(shopping_cart), 201


@_api.route('/<int:shopping_cart_id>')
class ShoppingCartResource(_ShoppingCartResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(shopping_cart_sw_model, envelope='data')
    @token_required
    def get(self, shopping_cart_id: int) -> tuple:
        shopping_cart = self._shopping_cart_service.find(shopping_cart_id)
        return shopping_cart_serializer.dump(shopping_cart), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(shopping_cart_input_sw_model)
    @_api.marshal_with(shopping_cart_sw_model, envelope='data')
    @token_required
    def put(self, shopping_cart_id: int) -> tuple:
        shopping_cart = self._shopping_cart_service.find(
            shopping_cart_id, **{'deleted_at': None}
        )
        self._shopping_cart_service.delete_books_relation(shopping_cart_id)

        request_payload = self._request_payload()
        request_payload['shopping_cart_id'] = shopping_cart.id
        shopping_cart_books = self._shopping_cart_book_service.create(
            **request_payload
        )

        book_ids = []
        for shopping_cart_book in shopping_cart_books:
            book_ids += [shopping_cart_book.book_id] * shopping_cart_book.units

        self._shopping_cart_service.manager.save(
            shopping_cart.id,
            **{'total_price': self._book_price_service.cal_price(book_ids)}
        )
        return shopping_cart_serializer.dump(shopping_cart), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(shopping_cart_sw_model, envelope='data')
    @token_required
    def delete(self, shopping_cart_id: int) -> tuple:
        book = self._shopping_cart_service.delete(shopping_cart_id)
        return shopping_cart_serializer.dump(book), 200


@_api.route('/search')
class ShoppingCartsSearchResource(_ShoppingCartResource):
    @_api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(shopping_cart_search_output_sw_model)
    @token_required
    def post(self) -> tuple:
        shopping_cart_data = self._shopping_cart_service.get(
            **self._request_payload()
        )
        shopping_cart_data_lst = list(shopping_cart_data['query'].items)
        return {
            'data': shopping_carts_serializer.dump(shopping_cart_data_lst),
            'records_total': shopping_cart_data['records_total'],
            'records_filtered': shopping_cart_data['records_filtered'],
        }, 200
