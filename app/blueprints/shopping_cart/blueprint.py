from flask import Blueprint

from .serializers import shopping_cart_serializer
from .serializers import shopping_carts_serializer
from .service import ShoppingCartService
from .swagger import shopping_cart_search_output_sw_model
from .swagger import shopping_cart_sw_model
from app.blueprints.base import BaseResource
from app.decorators import token_required
from app.extensions import api as root_api


blueprint = Blueprint('shopping_carts', __name__)
api = root_api.namespace(
    'shopping_carts', description='Shopping carts endpoints.'
)


class _ShoppingCartResource(BaseResource):
    shopping_cart_service = ShoppingCartService()


@api.route('')
class NewShoppingCartResource(_ShoppingCartResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(shopping_cart_sw_model)
    @api.marshal_with(shopping_cart_sw_model, envelope='data', code=201)
    @token_required
    def post(self) -> tuple:
        book = self.shopping_cart_service.create(**self.request_payload())
        return shopping_cart_serializer.dump(book), 201


@api.route('/<int:shopping_cart_id>')
class ShoppingCartResource(_ShoppingCartResource):
    @api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(shopping_cart_sw_model, envelope='data')
    @token_required
    def get(self, shopping_cart_id: int) -> tuple:
        shopping_cart = self.shopping_cart_service.find(shopping_cart_id)
        return shopping_cart_serializer.dump(shopping_cart), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.expect(shopping_cart_sw_model)
    @api.marshal_with(shopping_cart_sw_model, envelope='data')
    @token_required
    def put(self, shopping_cart_id: int) -> tuple:
        shopping_cart = self.shopping_cart_service.save(
            shopping_cart_id, **self.request_payload()
        )
        return shopping_cart_serializer.dump(shopping_cart), 200

    @api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(shopping_cart_sw_model, envelope='data')
    @token_required
    def delete(self, shopping_cart_id: int) -> tuple:
        book = self.shopping_cart_service.delete(shopping_cart_id)
        return shopping_cart_serializer.dump(book), 200


@api.route('/search')
class ShoppingCartsSearchResource(_ShoppingCartResource):
    @api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @api.marshal_with(shopping_cart_search_output_sw_model)
    @token_required
    def post(self) -> tuple:
        shopping_cart_data = self.shopping_cart_service.get(
            **self.request_payload()
        )
        shopping_cart_data_lst = list(shopping_cart_data['query'].items)
        return {
            'data': shopping_carts_serializer.dump(shopping_cart_data_lst),
            'records_total': shopping_cart_data['records_total'],
            'records_filtered': shopping_cart_data['records_filtered'],
        }, 200
