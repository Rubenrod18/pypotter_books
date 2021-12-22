import logging

from marshmallow import fields
from marshmallow import post_load
from marshmallow import pre_load
from marshmallow import ValidationError

from app.blueprints.base import TimestampField
from app.blueprints.book.manager import BookManager
from app.blueprints.shopping_cart import ShoppingCartBook
from app.blueprints.shopping_cart.manager import ShoppingCartManager
from app.extensions import ma

logger = logging.getLogger(__name__)

_book_manager = BookManager()
_shopping_cart_manager = ShoppingCartManager()


class ShoppingCartBookSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = ShoppingCartBook
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()
    shopping_cart_id = ma.auto_field()
    book_id = ma.auto_field()

    # Normal fields
    units = ma.auto_field()

    # Output fields
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)


class LoadShoppingCartBookSerializer(ma.Schema):
    shopping_cart_id = fields.Integer(required=True, load_only=True)
    book_ids = fields.List(fields.Integer, required=True, load_only=True)
    units = fields.List(fields.Integer, required=True, load_only=True)

    @staticmethod
    def __check_if_books_are_already_created(book_ids: list) -> None:
        for book_id in book_ids:
            if not _book_manager.find(book_id, **{'deleted_at': None}):
                ValidationError(
                    field_name='book_id',
                    message=[f'"{book_id}" Book ID not found.'],
                )

    @staticmethod
    def __check_if_book_ids_has_same_items_than_units(
        book_ids: list, units: list
    ) -> None:
        if len(book_ids) != len(units):
            raise ValidationError(
                field_name='book_ids',
                message=[
                    'The book ids field has not same quantity than units field'
                ],
            )

    @staticmethod
    def __check_exists_shopping_cart_id(shopping_cart_id: int) -> None:
        if (
            _shopping_cart_manager.find(
                shopping_cart_id, **{'deleted_at': None}
            )
            is None
        ):
            raise ValidationError(
                field_name='shopping_cart_id',
                message=['Shopping cart not found'],
            )

    @pre_load
    def pre_load_process(self, data: dict, **kwargs) -> dict:  # noqa
        self.__check_if_book_ids_has_same_items_than_units(
            data['book_ids'],
            data['units'],
        )
        self.__check_if_books_are_already_created(data['book_ids'])
        self.__check_exists_shopping_cart_id(data['shopping_cart_id'])
        return data

    @post_load
    def post_load_process(self, data: dict, **kwargs) -> list:  # noqa
        return [
            {
                'book_id': item,
                'shopping_cart_id': data['shopping_cart_id'],
                'units': data['units'][index],
            }
            for index, item in enumerate(data['book_ids'])
        ]


load_shopping_cart_book_serializer = LoadShoppingCartBookSerializer()
