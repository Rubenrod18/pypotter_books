from ...extensions import db
from .manager import ShoppingCartManager
from .serializers import shopping_cart_serializer
from app.blueprints.base import BaseService


class ShoppingCartService(BaseService):
    def __init__(self):
        super(ShoppingCartService, self).__init__()
        self.manager = ShoppingCartManager()
        self.shopping_cart_serializer = shopping_cart_serializer

    def create(self, **kwargs):
        serialized_data = self.shopping_cart_serializer.load(kwargs)
        shopping_cart = self.manager.create(**serialized_data)
        db.session.add(shopping_cart)
        db.session.flush()
        return shopping_cart
