from app.blueprints.base import TimestampField
from app.blueprints.book import Book
from app.extensions import ma


class BookSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = Book
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()

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
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)


book_serializer = BookSerializer()
books_serializer = BookSerializer(many=True)
