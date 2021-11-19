from app.blueprints.base import TimestampField
from app.blueprints.book import BookPrice
from app.extensions import ma


class BookPriceSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = BookPrice
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()

    # Normal fields
    book_id = ma.auto_field()
    country_id = ma.auto_field()
    vat = ma.auto_field()
    price = ma.auto_field()

    # Output fields
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)


book_price_serializer = BookPriceSerializer()
book_prices_serializer = BookPriceSerializer(many=True)
