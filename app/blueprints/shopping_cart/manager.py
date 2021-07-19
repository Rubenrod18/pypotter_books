from app.blueprints.base import BaseManager
from app.blueprints.shopping_cart import ShoppingCart


class ShoppingCartManager(BaseManager):
    def __init__(self):
        super(ShoppingCartManager, self).__init__()
        self.model = ShoppingCart
