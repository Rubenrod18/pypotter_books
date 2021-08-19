from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.bill import Bill


class _BillBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_BillBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/bills'
        self.bill = self.find_random_record(Bill, **{'deleted_at': None})
