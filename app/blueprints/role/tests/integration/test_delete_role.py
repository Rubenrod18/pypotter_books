from ._base_integration_test import _RoleBaseIntegrationTest


class TestDeleteRole(_RoleBaseIntegrationTest):
    def test_delete_role(self):
        with self.app.app_context():
            role_id = self.get_rand_role().id

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.delete(
                f'{self.base_path}/{role_id}', json={}, headers=auth_header
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(role_id, json_data.get('id'))
            self.assertIsNotNone(json_data.get('deleted_at'))
            self.assertEqual(
                json_data.get('deleted_at'), json_data.get('updated_at')
            )
