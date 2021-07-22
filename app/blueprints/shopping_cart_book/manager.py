from app.blueprints.base import BaseManager
from app.blueprints.shopping_cart import ShoppingCartBook


class ShoppingCartBookManager(BaseManager):
    def __init__(self):
        super(ShoppingCartBookManager, self).__init__()
        self.model = ShoppingCartBook
