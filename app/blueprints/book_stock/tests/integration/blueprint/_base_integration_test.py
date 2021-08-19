from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.book import BookStock


class _BookStockBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_BookStockBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/book_stocks'
        self.book_stock = self.find_random_record(
            BookStock, **{'deleted_at': None}
        )
