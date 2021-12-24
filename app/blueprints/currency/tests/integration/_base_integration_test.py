from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.currency.tests.factories import CurrencyFactory


class _CurrencyBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_CurrencyBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/currencies'
        self.currency = CurrencyFactory(deleted_at=None)
