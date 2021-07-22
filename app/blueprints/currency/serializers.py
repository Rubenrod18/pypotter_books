from app.blueprints.base import TimestampField
from app.blueprints.currency import Currency
from app.extensions import ma


class CurrencySerializer(ma.SQLAlchemySchema):
    class Meta:
        model = Currency
        ordered = True

    id = ma.auto_field()
    code = ma.auto_field()
    decimals = ma.auto_field()
    name = ma.auto_field()
    name_plural = ma.auto_field()
    num = ma.auto_field()
    symbol = ma.auto_field()
    symbol_native = ma.auto_field()

    # Output fields
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)


currency_serializer = CurrencySerializer()
currencies_serializer = CurrencySerializer(many=True)
