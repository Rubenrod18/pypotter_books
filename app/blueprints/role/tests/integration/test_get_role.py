from ._base_integration_test import _RoleBaseIntegrationTest


class TestGetRole(_RoleBaseIntegrationTest):
    def test_get_role(self):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.get(
            f'{self.base_path}/{self.role.id}', json={}, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.role.id, json_data.get('id'))
        self.assertEqual(
            self.role.label.lower().replace(' ', '_'), json_data.get('name')
        )
        self.assertEqual(self.role.label, json_data.get('label'))
        self.assertEqual(
            self.role.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('created_at'),
        )
        self.assertEqual(
            self.role.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('updated_at'),
        )
        self.assertEqual(self.role.deleted_at, json_data.get('deleted_at'))
