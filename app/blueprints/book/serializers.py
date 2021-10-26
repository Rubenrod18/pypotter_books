from marshmallow import fields

from app.blueprints.base import TimestampField
from app.blueprints.book import Book
from app.blueprints.book_price.serializers import BookPriceSerializer
from app.blueprints.book_stock.serializers import BookStockSerializer
from app.extensions import ma


class BookSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = Book
        ordered = True

    # Normal fields
    title = ma.auto_field()
    author = ma.auto_field()
    description = ma.auto_field()
    isbn = ma.auto_field()
    total_pages = ma.auto_field()
    publisher = ma.auto_field()
    published_date = ma.auto_field()
    language = ma.auto_field()
    dimensions = ma.auto_field()

    # Output fields
    id = ma.auto_field(dump_only=True)
    book_stocks = fields.List(
        fields.Nested(BookStockSerializer), dump_only=True
    )
    book_prices = fields.List(
        fields.Nested(BookPriceSerializer), dump_only=True
    )
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            'self': ma.URLFor(
                'books_book_resource', values=dict(book_id='<id>')
            ),
            'collection': ma.URLFor('books_books_search_resource'),
        }
    )


book_serializer = BookSerializer()
books_serializer = BookSerializer(many=True)
