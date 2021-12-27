from app.blueprints.base import BaseManager
from app.blueprints.shopping_cart import ShoppingCartBook


class ShoppingCartBookManager(BaseManager):
    def __init__(self):
        super(ShoppingCartBookManager, self).__init__()
        self.model = ShoppingCartBook

    def get_by_shopping_cart_id(self, shopping_cart_id: int):
        return self.model.query.filter(
            self.model.shopping_cart_id == shopping_cart_id
        )

    def remove_by_shopping_cart_id(self, shopping_cart_id: int) -> int:
        return self.model.query.filter(
            self.model.shopping_cart_id == shopping_cart_id
        ).delete()
