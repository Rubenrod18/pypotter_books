from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.role import Role


class _RoleBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_RoleBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/roles'
        self.role = self.find_random_record(Role, **{'deleted_at': None})
