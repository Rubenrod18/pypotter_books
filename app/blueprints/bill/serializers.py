from app.blueprints.base import TimestampField
from app.blueprints.bill import Bill
from app.extensions import ma


class BillSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = Bill
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()
    user_id = ma.auto_field()
    currency_id = ma.auto_field()
    shopping_cart_id = ma.auto_field()

    # Output fields
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)


bill_serializer = BillSerializer()
bills_serializer = BillSerializer(many=True)
