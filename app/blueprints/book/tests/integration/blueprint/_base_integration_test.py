from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.book.tests.factories import BookFactory


class _BookBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_BookBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/books'
        self.book = BookFactory(deleted_at=None)
