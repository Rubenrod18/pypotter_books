from app.blueprints.base import TimestampField
from app.blueprints.shopping_cart import ShoppingCart
from app.extensions import ma


class ShoppingCartSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = ShoppingCart
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()
    user_id = ma.auto_field()

    # Output fields
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)


shopping_cart_serializer = ShoppingCartSerializer()
shopping_carts_serializer = ShoppingCartSerializer(many=True)
