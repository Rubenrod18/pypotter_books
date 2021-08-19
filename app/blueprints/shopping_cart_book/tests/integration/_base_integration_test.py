from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.shopping_cart import ShoppingCartBook


class _ShoppingCartBookBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_ShoppingCartBookBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/shopping_cart_books'
        self.shopping_cart_book = self.find_random_record(
            ShoppingCartBook, **{'deleted_at': None}
        )
