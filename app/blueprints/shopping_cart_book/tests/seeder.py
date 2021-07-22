from app.blueprints.shopping_cart_book.tests.factory import (
    ShoppingCartBookFactory,
)
from app.decorators import seed_actions


class Seeder:
    name = 'ShoppingCartBookSeeder'
    priority = 9

    @seed_actions
    def __init__(self):
        ShoppingCartBookFactory.create_batch(10)
