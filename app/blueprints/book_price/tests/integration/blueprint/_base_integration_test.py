from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.book import BookPrice


class _BookPriceBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_BookPriceBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/book_prices'
        self.book_price = self.find_random_record(
            BookPrice, **{'deleted_at': None}
        )
