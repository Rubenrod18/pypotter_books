from ...extensions import db
from .manager import BookStockManager
from .serializers import book_stock_serializer
from app.blueprints.base import BaseService


class BookStockService(BaseService):
    def __init__(self):
        super(BookStockService, self).__init__()
        self.manager = BookStockManager()
        self.book_stock_serializer = book_stock_serializer

    def create(self, **kwargs):
        serialized_data = self.book_stock_serializer.load(kwargs)
        book_stock = self.manager.create(**serialized_data)
        db.session.add(book_stock)
        db.session.flush()
        return book_stock
