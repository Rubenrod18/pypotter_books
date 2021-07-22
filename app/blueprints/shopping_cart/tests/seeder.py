from app.blueprints.shopping_cart.tests.factory import (
    UserWithoutShoppingCartFactory,
)
from app.blueprints.shopping_cart.tests.factory import (
    UserWithShoppingCartFactory,
)
from app.decorators import seed_actions


class Seeder:
    name = 'ShoppingCartSeeder'
    priority = 7

    @seed_actions
    def __init__(self):
        self.__create_shopping_carts()

    @staticmethod
    def __create_shopping_carts():
        UserWithoutShoppingCartFactory.create_batch(2)
        UserWithShoppingCartFactory.create_batch(5)
