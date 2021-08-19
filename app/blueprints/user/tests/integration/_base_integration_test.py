from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.user import User


class _UserBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_UserBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/users'
        self.user = self.find_random_record(
            User, **{'deleted_at': None, 'active': True}
        )
