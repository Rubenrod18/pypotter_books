from app.blueprints.base import BaseService
from app.blueprints.book.manager import BookManager
from app.blueprints.book.serializers import book_serializer
from app.extensions import db


class BookService(BaseService):
    def __init__(self):
        super(BookService, self).__init__()
        self.manager = BookManager()
        self.book_serializer = book_serializer

    def create(self, **kwargs):
        serialized_data = self.book_serializer.load(kwargs)
        book = self.manager.create(**serialized_data)
        db.session.add(book)
        db.session.commit()
        return book
