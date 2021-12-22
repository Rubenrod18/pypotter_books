from typing import Union

from app.blueprints.base import BaseService
from app.blueprints.book.manager import BookManager
from app.blueprints.book_price.manager import BookPriceManager
from app.blueprints.book_price.serializers import book_price_serializer
from app.blueprints.book_price.services._cal_book_price_service import (
    _CalBookPriceService,
)
from app.extensions import db


class BookPriceService(BaseService):
    def __init__(self):
        super(BookPriceService, self).__init__()
        self._cal_book_price_service = _CalBookPriceService()
        self.manager = BookPriceManager()
        self.book_manager = BookManager()
        self.book_price_serializer = book_price_serializer

    def create(self, **kwargs):
        serialized_data = self.book_price_serializer.load(kwargs)
        book_price = self.manager.create(**serialized_data)
        db.session.add(book_price)
        db.session.flush()
        return book_price

    def cal_price(self, book_ids: list) -> Union[float, int]:
        """Calculate books price."""
        return self._cal_book_price_service.price(book_ids)
