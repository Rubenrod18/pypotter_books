from ._base_integration_test import _RoleBaseIntegrationTest


class TestDeleteRole(_RoleBaseIntegrationTest):
    def test_delete_role(self):
        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.delete(
            f'{self.base_path}/{self.role.id}', json={}, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code, msg=json_response)
        self.assertEqual(self.role.id, json_data.get('id'))
        self.assertIsNotNone(json_data.get('deleted_at'))
        self.assertEqual(
            json_data.get('deleted_at'), json_data.get('updated_at')
        )
