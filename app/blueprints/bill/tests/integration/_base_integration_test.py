from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.bill.tests.factories import BillFactory
from app.blueprints.currency.tests.factories import (
    CurrencyFactory,
)
from app.blueprints.shopping_cart.tests.factories import (
    ShoppingCartFactory,
)


class _BillBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_BillBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/bills'

        currency = CurrencyFactory(deleted_at=None)
        shopping_cart = ShoppingCartFactory(deleted_at=None)
        self.bill = BillFactory(
            currency_id=currency.id,
            deleted_at=None,
            shopping_cart_id=shopping_cart.id,
            user_id=shopping_cart.user_id,
        )
