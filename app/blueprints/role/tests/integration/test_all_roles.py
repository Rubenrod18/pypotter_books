from ... import RoleFactory
from ._base_integration_test import _RoleBaseIntegrationTest


class TestAllRoles(_RoleBaseIntegrationTest):
    def test_get_all_roles_created_roles_returns_roles(self):
        [RoleFactory(deleted_at=None) for _ in range(10)]

        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.get(
            self.base_path, json={}, headers=auth_header
        )
        json_response = response.get_json()

        self.assertEqual(200, response.status_code, msg=json_response)
        self.assertEqual(12, len(json_response.get('data')))
