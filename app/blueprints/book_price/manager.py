from app.blueprints.base import BaseManager
from app.blueprints.book import BookPrice


class BookPriceManager(BaseManager):
    def __init__(self):
        super(BookPriceManager, self).__init__()
        self.model = BookPrice
