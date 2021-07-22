from app.blueprints.base import BaseManager
from app.blueprints.book import BookStock


class BookStockManager(BaseManager):
    def __init__(self):
        super(BookStockManager, self).__init__()
        self.model = BookStock
