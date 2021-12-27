from app.blueprints.shopping_cart.tests.factories import (
    UserWithoutShoppingCartSeedFactory,
)
from app.blueprints.shopping_cart.tests.factories import (
    UserWithShoppingCartSeedFactory,
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
        UserWithoutShoppingCartSeedFactory.create_batch(2)
        UserWithShoppingCartSeedFactory.create_batch(5)
