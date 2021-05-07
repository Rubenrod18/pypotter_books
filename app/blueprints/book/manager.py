from app.blueprints.base import BaseManager
from app.blueprints.book import Book


class BookManager(BaseManager):
    def __init__(self):
        super(BookManager, self).__init__()
        self.model = Book
