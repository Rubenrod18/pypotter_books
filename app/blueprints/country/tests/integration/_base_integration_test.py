from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.country.tests.factories import CountryFactory


class _CountryBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_CountryBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/countries'
        self.country = CountryFactory(deleted_at=None)
