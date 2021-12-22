from app.blueprints.base import TimestampField
from app.blueprints.book import BookStock
from app.extensions import ma


class BookStockSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = BookStock
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()

    # Normal fields
    country_id = ma.auto_field()
    book_id = ma.auto_field()
    stock = ma.auto_field()

    # Output fields
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)


book_stock_serializer = BookStockSerializer()
book_stocks_serializer = BookStockSerializer(many=True)
