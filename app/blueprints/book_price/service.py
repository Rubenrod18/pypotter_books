from .manager import BookPriceManager
from .serializers import book_price_serializer
from app.blueprints.base import BaseService
from app.extensions import db


class BookPriceService(BaseService):
    def __init__(self):
        super(BookPriceService, self).__init__()
        self.manager = BookPriceManager()
        self.book_price_serializer = book_price_serializer

    def create(self, **kwargs):
        serialized_data = self.book_price_serializer.load(kwargs)
        book = self.manager.create(**serialized_data)
        db.session.add(book)
        db.session.commit()
        return book
