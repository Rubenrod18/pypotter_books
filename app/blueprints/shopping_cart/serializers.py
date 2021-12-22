from marshmallow import fields

from app.blueprints.base import TimestampField
from app.blueprints.shopping_cart import ShoppingCart
from app.blueprints.shopping_cart.manager import ShoppingCartManager
from app.extensions import ma

_shopping_cart_manager = ShoppingCartManager()


class ShoppingCartSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = ShoppingCart
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()
    user_id = ma.auto_field()
    total_price = ma.auto_field()

    # Output fields
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)

    # Relations
    books = fields.List(fields.Nested('ShoppingCartBookSerializer'))


shopping_cart_serializer = ShoppingCartSerializer()
shopping_carts_serializer = ShoppingCartSerializer(many=True)
