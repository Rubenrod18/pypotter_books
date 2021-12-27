from ...extensions import db
from .manager import ShoppingCartBookManager
from .serializers import load_shopping_cart_book_serializer
from app.blueprints.base import BaseService


class ShoppingCartBookService(BaseService):
    def __init__(self):
        super(ShoppingCartBookService, self).__init__()
        self.manager = ShoppingCartBookManager()

    def create(self, **kwargs) -> list:
        serialized_data = load_shopping_cart_book_serializer.load(kwargs)
        shopping_cart_books = []

        for item in serialized_data:
            shopping_cart_book = self.manager.create(**item)
            db.session.add(shopping_cart_book)
            db.session.flush()
            shopping_cart_books.append(shopping_cart_book)

        return shopping_cart_books
