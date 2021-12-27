from app.blueprints.base.tests.base_api_test import BaseApiTest
from app.blueprints.role import RoleFactory


class _RoleBaseIntegrationTest(BaseApiTest):
    def setUp(self):
        super(_RoleBaseIntegrationTest, self).setUp()
        self.base_path = f'{self.base_path}/roles'
        self.role = RoleFactory(deleted_at=None)
