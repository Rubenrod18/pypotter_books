from app.blueprints.base.tests.base_api_test import BaseApiTest


class _AuthBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_AuthBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/auth'
