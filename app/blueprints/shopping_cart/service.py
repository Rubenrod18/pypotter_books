from ...extensions import db
from ..shopping_cart_book.manager import ShoppingCartBookManager
from .manager import ShoppingCartManager
from .serializers import shopping_cart_serializer
from app.blueprints.base import BaseService


class ShoppingCartService(BaseService):
    def __init__(self):
        super(ShoppingCartService, self).__init__()
        self.manager = ShoppingCartManager()
        self.shopping_cart_book_manager = ShoppingCartBookManager()
        self.shopping_cart_serializer = shopping_cart_serializer

    def create(self, **kwargs):
        serialized_data = self.shopping_cart_serializer.load(kwargs)
        shopping_cart = self.manager.create(**serialized_data)
        db.session.add(shopping_cart)
        db.session.flush()
        return shopping_cart

    def delete_books_relation(self, shopping_cart_id: int) -> int:
        return self.shopping_cart_book_manager.remove_by_shopping_cart_id(
            shopping_cart_id
        )
