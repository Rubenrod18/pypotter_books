from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.shopping_cart.tests.factories import ShoppingCartFactory


class _ShoppingCartBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_ShoppingCartBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/shopping_carts'
        self.shopping_cart = ShoppingCartFactory(deleted_at=None)
