from app.blueprints.base import TimestampField
from app.blueprints.shopping_cart import ShoppingCartBook
from app.extensions import ma


class ShoppingCartBookSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = ShoppingCartBook
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()
    shopping_cart_id = ma.auto_field()
    book_id = ma.auto_field()

    # Normal fields
    discount = ma.auto_field()

    # Output fields
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)


shopping_cart_book_serializer = ShoppingCartBookSerializer()
shopping_cart_books_serializer = ShoppingCartBookSerializer(many=True)
