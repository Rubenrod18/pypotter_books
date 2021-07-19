from ...extensions import db
from .manager import ShoppingCartBookManager
from .serializers import shopping_cart_book_serializer
from app.blueprints.base import BaseService


class ShoppingCartBookService(BaseService):
    def __init__(self):
        super(ShoppingCartBookService, self).__init__()
        self.manager = ShoppingCartBookManager()

    def create(self, **kwargs):
        serialized_data = shopping_cart_book_serializer.load(kwargs)
        shopping_cart_book = self.manager.create(**serialized_data)
        db.session.add(shopping_cart_book)
        db.session.flush()
        return shopping_cart_book
